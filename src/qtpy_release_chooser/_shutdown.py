"""Optional shutdown helper."""
from __future__ import annotations

def terminate_child_processes(*args, **kwargs) -> None:
    try:
        from app_process_lifecycle.shutdown import terminate_child_processes as _t
        _t(*args, **kwargs)
    except Exception:
        pass
