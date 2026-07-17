"""Minimal progress dialog stub (host may replace)."""
from __future__ import annotations
from qtpy.QtWidgets import QProgressDialog

class ProgressDialog(QProgressDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
