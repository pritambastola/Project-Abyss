"""
Fast Command Router

Handles deterministic commands without using an LLM.
"""

from __future__ import annotations

from system.application_manager import ApplicationManager


class FastRouter:
    def __init__(self):
        self.app_manager = ApplicationManager()

    def execute(self, command: str) -> bool:
        command = command.lower().strip()

        # Open application
        if command.startswith("open "):
            app = command.replace("open ", "", 1).strip()
            return self.app_manager.open(app)

        return False

    def close(self):
        self.app_manager.close_database()