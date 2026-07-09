from database.database import Database


def create_schema():
    db = Database()

    db.execute("""
    CREATE TABLE IF NOT EXISTS applications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        aliases TEXT,
        executable TEXT,
        shortcut TEXT,
        launch_count INTEGER DEFAULT 0,
        last_launched TEXT
    )
    """)

    db.close()