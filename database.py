import sqlite3
import logging
import os

logger = logging.getLogger(__name__)

DB_PATH = os.path.join("data", "leads.db")


def init_db() -> None:
    """Initialize the SQLite database and create the leads table if needed."""
    os.makedirs("data", exist_ok=True)
    try:
        con = sqlite3.connect(DB_PATH)
        con.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT,
                phone   TEXT,
                email   TEXT,
                website TEXT,
                rating  REAL,
                score   INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        con.commit()
        logger.info("Database initialized at %s", DB_PATH)
    except sqlite3.Error as e:
        logger.error("Failed to initialize database: %s", e)
    finally:
        con.close()


def save_leads(leads: list[dict]) -> None:
    """Persist a list of lead dicts to the database."""
    if not leads:
        return
    try:
        con = sqlite3.connect(DB_PATH)
        con.executemany(
            "INSERT INTO leads (name, phone, email, website, rating, score) "
            "VALUES (:name, :phone, :email, :website, :rating, :score)",
            leads,
        )
        con.commit()
        logger.info("Saved %d leads to database.", len(leads))
    except sqlite3.Error as e:
        logger.error("Failed to save leads: %s", e)
    finally:
        con.close()
