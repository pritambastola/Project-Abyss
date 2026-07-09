"""
Shortcut Resolver

Resolves a Windows .lnk shortcut to its target executable.
"""

from pathlib import Path

import win32com.client


class ShortcutResolver:
    def __init__(self):
        self.shell = win32com.client.Dispatch("WScript.Shell")

    def resolve(self, shortcut: str | Path) -> str | None:
        shortcut = str(shortcut)

        try:
            link = self.shell.CreateShortcut(shortcut)

            target = link.TargetPath

            if target:
                return target

            return None

        except Exception:
            return None