import sqlite3
from utils.db import connect_db, create_expenses_table, create_budgets_table, drop_tables

def migrate_database():
    """Run the migration to update the database schema."""
    # Connect to the actual database
    conn = connect_db()
    cursor = conn.cursor()

    # Drop existing tables (if necessary) to ensure the schema is updated
    drop_tables()

    # Create the tables with the updated schema
    create_expenses_table()
    create_budgets_table()

    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate_database()
