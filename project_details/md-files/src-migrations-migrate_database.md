# src\migrations\migrate_database.py

## General description
This Python script is responsible for migrating the database schema for the Passive Expenses Bot. The script is used to reset and recreate the expenses and budgets tables in the database by dropping the existing tables (if necessary) and applying the updated schema.
This script manages the migration of the database schema for an application. It includes functions for dropping existing tables and creating new ones to keep the database up-to-date.

## Pseudocode

```
### Step 1: Add 'src' Directory to System Path
1. Get the directory path of the current file.
2. Append the `src` directory to the system path.
3. Import the `connect_db` function from `utils.db`.

### Step 2: Define Table Functions

#### Function: `create_user_language_table(cursor)`
- **Purpose:** Create a table named `user_language` to store user language preferences.
- **Steps:**
  1. Execute SQL to create the `user_language` table if it doesn't already exist.
  2. Print success message.

#### Function: `create_expenses_table(cursor)`
- **Purpose:** Create the `expenses` table to track user expenses.
- **Steps:**
  1. Execute SQL to create the `expenses` table if it doesn't already exist.
  2. Print success message.

#### Function: `create_budgets_table(cursor)`
- **Purpose:** Create the `budgets` table to manage user budgets.
- **Steps:**
  1. Execute SQL to create the `budgets` table if it doesn't already exist.
  2. Print success message.

#### Function: `drop_tables(cursor)`
- **Purpose:** Drop the existing tables (`expenses`, `budgets`, `user_language`) if they exist.
- **Steps:**
  1. Execute SQL to drop `expenses` table.
  2. Execute SQL to drop `budgets` table.
  3. Execute SQL to drop `user_language` table.
  4. Print success message.

### Step 3: Migrate the Database

#### Function: `migrate_database()`
- **Purpose:** Run the migration to update the database schema.
- **Steps:**
  1. Connect to the database using `connect_db()`.
  2. Create a cursor for executing SQL commands.
  3. Call `drop_tables(cursor)` to remove old tables.
  4. Call `create_expenses_table(cursor)` to create the `expenses` table.
  5. Call `create_budgets_table(cursor)` to create the `budgets` table.
  6. Call `create_user_language_table(cursor)` to create the `user_language` table.
  7. Print migration complete message.
  8. Commit changes to the database.
  9. Close the database connection.

### Step 4: Main Execution Block
- **Purpose:** Run the migration when the script is executed directly.
- **Steps:**
  1. Call `migrate_database()` to perform the migration.
```

## Code 

```
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


```