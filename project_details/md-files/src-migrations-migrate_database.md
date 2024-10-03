# src\migrations\migrate_database.py

## General description
This Python script is responsible for migrating the database schema for the Passive Expenses Bot. The script is used to reset and recreate the expenses and budgets tables in the database by dropping the existing tables (if necessary) and applying the updated schema.

## Pseudocode for Each Section 

1. Database Connection and Setup
```
Import Modules:

Import the necessary functions from db.py:
connect_db(): Establishes a connection to the SQLite database.
create_expenses_table(): Recreates the expenses table based on the updated schema.
create_budgets_table(): Recreates the budgets table based on the updated schema.
drop_tables(): Drops existing tables to reset the schema.

```

2. Migration Function
```
Function: migrate_database()

Purpose: This function is responsible for running the database migration, ensuring the schema is updated.
Steps:
Connect to the database using connect_db() to establish a connection.
Drop the existing tables using drop_tables(), resetting the schema.
Recreate the tables using:
create_expenses_table(): Recreates the expenses table with the updated columns.
create_budgets_table(): Recreates the budgets table with the updated columns.
Commit the changes to the database and close the connection.

```

3. Script Execution
```
Main Execution Block:

Purpose: This part ensures that the script can be executed directly from the command line.
Steps:
If the script is run as the main program (__name__ == "__main__"), it calls the migrate_database() function.
This will apply the database schema changes by dropping the existing tables and recreating them with the latest schema.
```

## Code 

```
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

```