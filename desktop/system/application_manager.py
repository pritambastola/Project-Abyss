"""
Application Manager

Launches and manages desktop applications.
"""

from __future__ import annotations

import subprocess
from datetime import datetime

from core.logger import logger
from database.database import Database


class ApplicationManager:
    def __init__(self):
        self.db = Database()

    def open(self, app_name: str) -> bool:

        app_name = app_name.lower().strip()

        apps = self.db.fetchall("""
            SELECT name, aliases, executable
            FROM applications
        """)

        executable = None
        matched_name = None

        for name, aliases, exe in apps:

            alias_list = [
                alias.strip().lower()
                for alias in (aliases or "").split(",")
                if alias.strip()
            ]

            if app_name in alias_list:
                executable = exe
                matched_name = name
                break

        if executable is None:
            logger.error(f"Application '{app_name}' not found.")
            return False

        try:

            subprocess.Popen(executable)

            self.db.execute(
                """
                UPDATE applications
                SET launch_count = launch_count + 1,
                    last_launched = ?
                WHERE name = ?
                """,
                (
                    datetime.now().isoformat(timespec="seconds"),
                    matched_name,
                ),
            )

            logger.info(f"Opened {matched_name}")

            return True

        except Exception as e:
            logger.exception(e)
            return False

    def close(self):
        pass

    def is_running(self):
        pass

    def focus(self):
        pass

    def close_database(self):
        self.db.close()