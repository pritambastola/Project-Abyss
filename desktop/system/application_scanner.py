"""
Application Scanner
"""

from pathlib import Path

from core.logger import logger
from database.database import Database
from system.shortcut_resolver import ShortcutResolver


class ApplicationScanner:
    def __init__(self):
        self.db = Database()
        self.resolver = ShortcutResolver()
        self.count = 0

    def scan_folder(self, folder: Path):

        if not folder.exists():
            return

        for shortcut in folder.rglob("*.lnk"):

            name = shortcut.stem.lower().strip()

            executable = self.resolver.resolve(shortcut)

            self.db.execute(
                """
                INSERT OR REPLACE INTO applications
                (name, executable, shortcut)
                VALUES (?, ?, ?)
                """,
                (
                    name,
                    executable,
                    str(shortcut)
                )
            )

            self.count += 1

    def scan(self):

        user = (
            Path.home()
            / "AppData"
            / "Roaming"
            / "Microsoft"
            / "Windows"
            / "Start Menu"
            / "Programs"
        )

        common = Path(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        )

        self.scan_folder(user)
        self.scan_folder(common)

        logger.info(f"Scanned {self.count} shortcuts.")

        total = self.db.fetchone(
            "SELECT COUNT(*) FROM applications"
        )[0]

        logger.info(f"{total} applications stored.")

        self.db.close()