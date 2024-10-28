import sqlite3
import logging
import os
from src.utils.lang import translate

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to the database (adjust if necessary)
DB_PATH = "src/database/expenses.db"

# Set the language for translation (adjust as needed or make it dynamic)
LANGUAGE = "en"

def create_reports_table(conn):
    """
    Creates the 'reports' table in the database if it doesn't already exist.
    Fields include:
    - report_id: Primary key (auto-incremented)
    - user_id: ID of the user who created the report
    - creation_date: Date when the report was created
    - filters: Filters used to generate the report
    - file_path: Path to the generated report file
    """
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reports (
                    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    filters TEXT,
                    file_path TEXT NOT NULL
                )
            ''')
            logger.info(translate("reports_table_created", language=LANGUAGE))
    except sqlite3.Error as e:
        logger.error(translate("error_creating_table", language=LANGUAGE, error=str(e)))

def drop_reports_table(conn):
    """
    Drops the 'reports' table from the database if it exists.
    This is used for rollback purposes in case of migration failure.
    """
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''
                DROP TABLE IF EXISTS reports
            ''')
            logger.info(translate("reports_table_dropped", language=LANGUAGE))
    except sqlite3.Error as e:
        logger.error(translate("error_dropping_table", language=LANGUAGE, error=str(e)))

def migrate():
    """
    Performs the migration to add the 'reports' table to the database.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            create_reports_table(conn)
    except sqlite3.Error as e:
        logger.error(translate("error_connecting_db", language=LANGUAGE, error=str(e)))

def rollback():
    """
    Rolls back the migration by removing the 'reports' table from the database.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            drop_reports_table(conn)
    except sqlite3.Error as e:
        logger.error(translate("error_connecting_db", language=LANGUAGE, error=str(e)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "rollback":
        rollback()
    else:
        migrate()
