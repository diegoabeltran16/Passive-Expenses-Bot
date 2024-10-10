# src/utils/db.py

## General description
The main goal of this code is to manage the SQLite database for storing, retrieving, updating, and deleting expense and budget information for a financial tracking application. The code includes functions for creating tables, managing user expenses, managing budgets, and handling user language preferences.

## Pseudocode
```
1. **connect_db function:**
   - Try to connect to SQLite database ('expenses.db').
   - If connection is successful, create necessary tables (expenses, budgets, user_language).
   - Return the connection object.
   - If connection fails, print error message and return `None`.

2. **create_expenses_table function:**
   - Create 'expenses' table if it does not exist, with columns for id, user_id, amount, description, category, and date_added.
   - Commit the changes to the database.
   - If an error occurs, print the error message and rollback the changes.

3. **create_budgets_table function:**
   - Create 'budgets' table if it does not exist, with columns for id, user_id, category, limit, period, start_date, and end_date.
   - Commit the changes to the database.
   - If an error occurs, print the error message and rollback the changes.

4. **create_user_language_table function:**
   - Create 'user_language' table if it does not exist, with columns for user_id and language.
   - Commit the changes to the database.
   - If an error occurs, print the error message and rollback the changes.

5. **insert_expense function:**
   - Insert a new expense into the 'expenses' table with user_id, amount, description, and optional category.
   - Commit the changes and return the ID of the newly inserted expense.
   - If an error occurs, print the error message, rollback changes, and return `None`.

6. **delete_expense function:**
   - Delete an expense from the 'expenses' table using the expense ID.
   - Commit the changes to the database.
   - If an error occurs, print the error message and rollback the changes.

7. **update_expense function:**
   - Update the amount and description of an expense in the 'expenses' table using the expense ID.
   - Commit the changes to the database.
   - If an error occurs, print the error message and rollback the changes.

8. **update_expense_category function:**
   - Update the category of an existing expense in the 'expenses' table.
   - Commit the changes to the database.
   - If an error occurs, print the error message and rollback the changes.

9. **get_expenses_by_user function:**
   - Retrieve all expenses for a specific user from the 'expenses' table using the user ID.
   - Return the list of expenses.
   - If an error occurs, print the error message and return an empty list.

10. **get_expenses_by_category function:**
    - Retrieve all expenses by category for a specific user.
    - Optionally filter by date range using start_date and end_date.
    - Return the list of expenses.
    - If an error occurs, print the error message and return an empty list.

11. **list_expenses function:**
    - Retrieve all expenses for a specific user from the 'expenses' table.
    - Return the list of expenses.
    - If an error occurs, print the error message and return an empty list.

12. **insert_budget function:**
    - Insert a new budget into the 'budgets' table with user_id, category, limit, period, start_date, and end_date.
    - Commit the changes to the database.
    - If an error occurs, print the error message and rollback the changes.

13. **get_budget_by_category function:**
    - Retrieve a budget for a specific category and user from the 'budgets' table.
    - Return the budget record.
    - If an error occurs, print the error message and return `None`.

14. **update_budget function:**
    - Update the limit of an existing budget in the 'budgets' table using the budget ID.
    - Commit the changes to the database.
    - If an error occurs, print the error message and rollback the changes.

```


## Code

```
import sqlite3

def connect_db():
    """
    Establishes a connection to the SQLite database and creates necessary tables if they don't exist.
    Returns the database connection object.
    """
    try:
        conn = sqlite3.connect('src/database/expenses.db')
        create_expenses_table(conn)
        create_budgets_table(conn)
        create_user_language_table(conn)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_expenses_table(conn):
    """Creates the 'expenses' table in the database if it doesn't already exist."""
    try:
        cursor = conn.cursor()
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
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating expenses table: {e}")
        conn.rollback()

def create_budgets_table(conn):
    """Creates the 'budgets' table in the database if it doesn't already exist."""
    try:
        cursor = conn.cursor()
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
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating budgets table: {e}")
        conn.rollback()

def create_user_language_table(conn):
    """Creates the 'user_language' table in the database if it doesn't already exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_language (
                user_id INTEGER PRIMARY KEY,
                language TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating user_language table: {e}")
        conn.rollback()

def insert_expense(conn, user_id, amount, description, category=None):
    """Inserts a new expense into the 'expenses' table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (user_id, amount, description, category)
            VALUES (?, ?, ?, ?)
        ''', (user_id, amount, description, category))
        conn.commit()
        return cursor.lastrowid  # Return the ID of the newly inserted expense
    except sqlite3.Error as e:
        print(f"Error inserting expense: {e}")
        conn.rollback()
        return None

def delete_expense(conn, expense_id):
    """Deletes an expense by its ID."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM expenses WHERE id = ?
        ''', (expense_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting expense: {e}")
        conn.rollback()

def update_expense(conn, expense_id, new_amount, new_description):
    """Updates the amount and description of an existing expense."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE expenses
            SET amount = ?, description = ?
            WHERE id = ?
        ''', (new_amount, new_description, expense_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating expense: {e}")
        conn.rollback()

def update_expense_category(conn, expense_id, category):
    """Updates the category of an existing expense."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE expenses
            SET category = ?
            WHERE id = ?
        ''', (category, expense_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating expense category: {e}")
        conn.rollback()

def get_expenses_by_user(conn, user_id):
    """Retrieves all expenses for a specific user."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM expenses WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving expenses: {e}")
        return []

def get_expenses_by_category(conn, user_id, category, start_date=None, end_date=None):
    """Retrieves all expenses by category for a specific user."""
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM expenses WHERE category = ? AND user_id = ?'
        params = [category, user_id]

        if start_date and end_date:
            query += ' AND date_added BETWEEN ? AND ?'
            params.extend([start_date, end_date])

        cursor.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving expenses by category: {e}")
        return []

def list_expenses(conn, user_id):
    """Lists all expenses for a specific user."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM expenses WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error listing expenses: {e}")
        return []

def insert_budget(conn, user_id, category, limit, period, start_date, end_date):
    """Inserts a new budget into the 'budgets' table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO budgets (user_id, category, "limit", period, start_date, end_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, category, limit, period, start_date, end_date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting budget: {e}")
        conn.rollback()

def get_budget_by_category(conn, user_id, category):
    """Retrieves the budget for a specific category and user."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM budgets WHERE user_id = ? AND category = ?
        ''', (user_id, category))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error retrieving budget: {e}")
        return None

def update_budget(conn, budget_id, new_limit):
    """Updates the limit of an existing budget."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE budgets
            SET "limit" = ?
            WHERE id = ?
        ''', (new_limit, budget_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating budget: {e}")
        conn.rollback()

```

## Testing 
tests/test_database.py

**Main Goal:**
The main goal of this code is to test the functionality of several database operations, including inserting and updating budgets and expenses in an in-memory SQLite database, ensuring that the operations work as expected.

### Testing Pseudocode
```
1. **Define a Test Class for Database Operations**
   - Import `unittest` and `sqlite3` libraries for testing.
   - Import relevant functions from the `db` module.

2. **Define Class `TestDatabaseOperations(unittest.TestCase)`**

   - **Method: `setUp()`**
     - Create an in-memory SQLite database connection before each test to ensure a clean environment.
     - Create the `expenses` and `budgets` tables.

   - **Method: `tearDown()`**
     - Close the database connection after each test.

3. **Test Cases:**

   - **Test: `test_insert_budget()`**
     - Insert a new budget into the database using `insert_budget()`.
     - Retrieve the budget by category using `get_budget_by_category()`.
     - Assert that the budget is not `None` and verify that the values match the expected inputs (category and limit).

   - **Test: `test_update_budget()`**
     - Insert a budget into the database.
     - Retrieve the budget by category.
     - Update the budget using `update_budget()` with a new limit.
     - Retrieve the updated budget and verify that the new limit is correctly updated.

   - **Test: `test_update_expense_category()`**
     - Insert an expense with a valid category using `insert_expense()`.
     - Retrieve expenses for a specific category using `get_expenses_by_category()` and assert that expenses are found.
     - Update the expense category using `update_expense_category()`.
     - Retrieve the updated expense by the new category and verify that the category update was successful.

4. **Main Execution Block:**
   - Run all the test cases by invoking `unittest.main()`.

```

### Testing Code
```
import unittest
import sqlite3
from src.utils.db import (
    insert_budget, get_budget_by_category, update_budget, insert_expense, 
    update_expense_category, get_expenses_by_category, create_expenses_table, create_budgets_table
)

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        """Set up a clean in-memory database before each test."""
        self.conn = sqlite3.connect(':memory:')  # Use in-memory database for testing
        create_expenses_table(self.conn)
        create_budgets_table(self.conn)

    def tearDown(self):
        """Close the connection after each test."""
        self.conn.close()

    # Test for budget insertion
    def test_insert_budget(self):
        insert_budget(self.conn, 1, "Food", 500.0, "monthly", "2023-01-01", "2023-01-31")
        budget = get_budget_by_category(self.conn, 1, "Food")
        self.assertIsNotNone(budget)
        self.assertEqual(budget[2], "Food")
        self.assertEqual(budget[3], 500.0)

    # Test for updating a budget
    def test_update_budget(self):
        insert_budget(self.conn, 1, "Food", 500.0, "monthly", "2023-01-01", "2023-01-31")
        budget = get_budget_by_category(self.conn, 1, "Food")
        update_budget(self.conn, budget[0], 600.0)
        updated_budget = get_budget_by_category(self.conn, 1, "Food")
        self.assertEqual(updated_budget[3], 600.0)

    # Test for inserting and categorizing expenses
    def test_update_expense_category(self):
        # Insert an expense with a valid category
        insert_expense(self.conn, 1, 50.0, "Groceries", category="Groceries")
        
        # Retrieve expenses before updating category
        expenses = get_expenses_by_category(self.conn, 1, "Groceries")
        self.assertGreater(len(expenses), 0, "No expenses found for user 1 before update")
        
        # Update the expense category
        if expenses:
            expense_id = expenses[0][0]  # Get the ID of the inserted expense
            update_expense_category(self.conn, expense_id, "Food")
        
            # Retrieve expenses after updating category
            categorized_expenses = get_expenses_by_category(self.conn, 1, "Food")
            self.assertGreater(len(categorized_expenses), 0, "Expense category update failed")

if __name__ == "__main__":
    unittest.main()
```