"""Processor architecture helper (vendored)."""
from __future__ import annotations
import platform
from enum import Enum

class ProcessorArchitecture(Enum):
    X86 = "x86"
    AMD64 = "amd64"
    ARM = "arm"
    ARM64 = "arm64"
    UNKNOWN = "unknown"

    @classmethod
    def from_os(cls) -> "ProcessorArchitecture":
        m = platform.machine().lower()
        if m in ("x86_64", "amd64"):
            return cls.AMD64
        if m in ("i386", "i686", "x86"):
            return cls.X86
        if m in ("arm64", "aarch64"):
            return cls.ARM64
        if m.startswith("arm"):
            return cls.ARM
        return cls.UNKNOWN
