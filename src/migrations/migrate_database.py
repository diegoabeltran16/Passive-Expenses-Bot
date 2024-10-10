import sys
import os

# Add the 'src' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.db import connect_db  # Import after the path has been updated

# Updated functions (same as before)
def create_user_language_table(cursor):
    """Creates the 'user_language' table to store user language preferences."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_language (
            user_id INTEGER PRIMARY KEY,
            language TEXT NOT NULL
        )
    ''')
    print("user_language table created successfully.")

def create_expenses_table(cursor):
    """Creates the 'expenses' table in the database if it doesn't already exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("Expenses table created successfully.")

def create_budgets_table(cursor):
    """Creates the 'budgets' table in the database if it doesn't already exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            "limit" REAL NOT NULL,
            period TEXT NOT NULL,
            start_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL
        )
    ''')
    print("Budgets table created successfully.")

def drop_tables(cursor):
    """Drops the expenses, budgets, and user_language tables if they exist."""
    cursor.execute('DROP TABLE IF EXISTS expenses')
    cursor.execute('DROP TABLE IF EXISTS budgets')
    cursor.execute('DROP TABLE IF EXISTS user_language')
    print("Tables dropped successfully.")

def migrate_database():
    """Run the migration to update the database schema."""
    # Connect to the actual database
    conn = connect_db()
    cursor = conn.cursor()

    # Drop existing tables (if necessary) to ensure the schema is updated
    drop_tables(cursor)

    # Create the tables with the updated schema
    create_expenses_table(cursor)
    create_budgets_table(cursor)
    create_user_language_table(cursor)

    print("Migration complete.")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate_database()
