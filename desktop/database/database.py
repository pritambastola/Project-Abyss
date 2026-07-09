from pathlib import Path
import sqlite3


class Database:
    def __init__(self):
        db_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "project_abyss.db"
        )

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()