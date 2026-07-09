"""
Application Indexer

Generates aliases for applications.
"""

from database.database import Database


class ApplicationIndexer:

    def __init__(self):
        self.db = Database()

    def generate_aliases(self):

        apps = self.db.fetchall(
            """
            SELECT id, name
            FROM applications
            """
        )

        for app_id, name in apps:

            aliases = self.create_aliases(name)

            self.db.execute(
                """
                UPDATE applications
                SET aliases=?
                WHERE id=?
                """,
                (
                    ",".join(sorted(aliases)),
                    app_id
                )
            )

    def create_aliases(self, name: str):

        name = name.lower()

        aliases = {name}

        words = name.split()

        aliases.update(words)

        replacements = {
            "visual studio code": ["code", "vscode"],
            "google chrome": ["chrome", "browser"],
            "microsoft edge": ["edge"],
            "spotify": ["music"],
            "discord": ["chat"],
            "steam": ["games"],
        }

        if name in replacements:
            aliases.update(replacements[name])

        return aliases

    def close(self):
        self.db.close()