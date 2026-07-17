"""Smoke import test."""

def test_import():
    from qtpy_release_chooser import configure
    assert callable(configure)
