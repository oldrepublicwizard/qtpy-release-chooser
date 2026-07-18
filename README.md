# qtpy-release-chooser

Qt dialog for picking a GitHub release, fork, or update channel.

Call `configure(...)` once with your program name, repo, and whatever else the dialog needs. Don't hard-code another app's config module into it.

Depends on `qtpy` plus a real binding (PyQt5/6 or PySide).

## Install

```bash
pip install git+https://github.com/oldrepublicwizard/qtpy-release-chooser.git
pip install qtpy PyQt5  # or PySide6, etc.
```

## License

LGPL-3.0-or-later
