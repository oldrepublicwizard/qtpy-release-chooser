"""Host-injected program info for the release chooser.

Call ``configure(...)`` once at app startup before opening dialogs.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, Optional

LOCAL_PROGRAM_INFO: Dict[str, Any] = {
    "currentVersion": "0.0.0",
    "repoOwner": "",
    "repoName": "",
    "programName": "App",
}

_is_remote_newer: Optional[Callable[[str, str], bool]] = None
_tag_to_version: Optional[Callable[[str], str]] = None
_version_to_tag: Optional[Callable[[str], str]] = None
_translate: Optional[Callable[..., str]] = None


def configure(
    *,
    program_info: Dict[str, Any] | None = None,
    is_remote_version_newer: Callable[[str, str], bool] | None = None,
    tag_to_version: Callable[[str], str] | None = None,
    version_to_tag: Callable[[str], str] | None = None,
    translate: Callable[..., str] | None = None,
) -> None:
    global LOCAL_PROGRAM_INFO, _is_remote_newer, _tag_to_version, _version_to_tag, _translate
    if program_info:
        LOCAL_PROGRAM_INFO.update(program_info)
    _is_remote_newer = is_remote_version_newer
    _tag_to_version = tag_to_version
    _version_to_tag = version_to_tag
    _translate = translate


def is_remote_version_newer(remote: str, local: str) -> bool:
    if _is_remote_newer:
        return _is_remote_newer(remote, local)
    return remote != local and remote > local


def toolset_tag_to_version(tag: str) -> str:
    if _tag_to_version:
        return _tag_to_version(tag)
    return tag.lstrip("vV")


def version_to_toolset_tag(version: str) -> str:
    if _version_to_tag:
        return _version_to_tag(version)
    return f"v{version}"


def translate(text: str, *args, **kwargs) -> str:
    if _translate:
        return _translate(text, *args, **kwargs)
    return text


def trf(text: str, *args, **kwargs) -> str:
    return translate(text, *args, **kwargs)
