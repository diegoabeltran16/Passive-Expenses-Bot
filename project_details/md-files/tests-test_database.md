# tests\test_database.py

## General description
This script defines unit tests for the Passive Expenses Bot’s database operations. It uses Python’s unittest framework to test various CRUD operations (Create, Read, Update, Delete) on the expenses and budgets tables. The tests ensure that the functions defined in the db.py module (inserting budgets, updating budgets, inserting expenses, etc.) behave correctly. An in-memory SQLite database is used for testing, so no external database file is needed, and all operations are reset after each test.

## Pseudocode for Each Section 

1. Imports and Setup
```
Import Modules:

Import unittest for creating test cases.
Import sys and os to manipulate the system path, allowing access to the db.py file.
Import necessary functions from the utils.db module:
CRUD operations: insert_budget(), update_budget(), insert_expense(), etc.
Table management: create_expenses_table(), create_budgets_table(), and drop_tables().

```

2. Database Setup and Teardown
```
Method: setUp()

Purpose: Sets up the in-memory database before each test.
Steps:
Connect to an in-memory SQLite database using sqlite3.connect(':memory:').
Drop existing tables using drop_tables() to ensure a clean schema.
Recreate the expenses and budgets tables using create_expenses_table() and create_budgets_table().
Method: tearDown()

Purpose: Closes the database connection after each test.
```

3. Test Cases
```
Test Case: test_insert_budget()

Purpose: Tests inserting a budget into the budgets table and retrieving it.
Steps:
Insert a budget for the user (user ID: 1) in the "Food" category.
Retrieve the inserted budget using get_budget_by_category().
Assert that the budget exists and that its fields (category and limit) are correct.
Test Case: test_update_budget()

Purpose: Tests updating an existing budget's limit.
Steps:
Insert a budget for the user (user ID: 1).
Update the budget’s limit to a new value.
Retrieve the updated budget and assert that the limit has been updated correctly.
Test Case: test_update_expense_category()

Purpose: Tests inserting an expense and updating its category.
Steps:
Insert an expense for the user (user ID: 1) without a category.
Update the expense’s category to "Food" using update_expense_category().
Retrieve the expense by category and assert that the category has been updated.

```

4. Higher-Level Logic Tests
```
Test Case: test_check_budget_status()

Purpose: Tests checking whether the total expenses for a category exceed the user’s budget.
Steps:
Insert a budget for the "Food" category.
Insert multiple expenses for "Food" and check if the total exceeds the budget.
Assert that the returned status indicates the budget has been exceeded.
Test Case: test_generate_expense_report()

Purpose: Tests generating an expense report for a user within a specified period.
Steps:
Insert expenses in different categories (e.g., "Food" and "Education").
Generate an expense report for the given period using generate_expense_report().
Assert that the report contains correct totals for each category.

```

5. Main Execution Block
```
Main Execution:

Purpose: If the script is run directly, it will execute all defined test cases.
Steps:
Call unittest.main() to automatically discover and run all test cases defined in the script.

```

## Code

```
import unittest
import sys
import os
import sqlite3

# Add the 'src' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from utils.db import (
    insert_budget, get_budget_by_category, update_budget, delete_budget,
    insert_expense, update_expense_category, get_expenses_by_category,
    create_expenses_table, create_budgets_table, drop_tables
)

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        """Set up a clean database before each test."""
        self.conn = sqlite3.connect(':memory:')  # Use in-memory database for testing
        self.cursor = self.conn.cursor()

        # Drop tables if they already exist to reset the database schema
        drop_tables()

        # Recreate the tables after dropping them
        create_expenses_table()
        create_budgets_table()

    def tearDown(self):
        """Close the connection after each test."""
        self.conn.close()

    # Test for budget insertion
    def test_insert_budget(self):
        insert_budget(1, "Food", 500.0, "monthly", "2023-01-01", "2023-01-31")
        budget = get_budget_by_category(1, "Food")
        self.assertIsNotNone(budget)
        self.assertEqual(budget[2], "Food")
        self.assertEqual(budget[3], 500.0)

    # Test for updating a budget
    def test_update_budget(self):
        insert_budget(1, "Food", 500.0, "monthly", "2023-01-01", "2023-01-31")
        budget = get_budget_by_category(1, "Food")
        update_budget(budget[0], 600.0)
        updated_budget = get_budget_by_category(1, "Food")
        self.assertEqual(updated_budget[3], 600.0)

    # Test for inserting and categorizing expenses
def test_update_expense_category(self):
    insert_expense(1, 50.0, "Groceries")  # Pass the user_id (1 in this case)
    expenses = get_expenses_by_category(1, None)  # No category yet
    update_expense_category(expenses[0][0], "Food")
    categorized_expenses = get_expenses_by_category(1, "Food")
    self.assertGreater(len(categorized_expenses), 0)

# Test for budget status checking
def test_check_budget_status(self):
    insert_budget(1, "Food", 500.0, "monthly", "2023-01-01", "2023-01-31")
    insert_expense(1, 100.0, "Groceries", "Food")
    insert_expense(1, 450.0, "Dining out", "Food")
    
    status = check_budget_status(1, "Food", "2023-01-01", "2023-01-31")
    self.assertIn("exceeded", status)  # Should exceed the budget

# Test for expense report generation
def test_generate_expense_report(self):
    insert_expense(1, 50.0, "Groceries", "Food")
    insert_expense(1, 100.0, "Dining out", "Food")
    insert_expense(1, 200.0, "Books", "Education")
    
    report = generate_expense_report(1, "2023-01-01", "2023-01-31")
    self.assertIn("Food: 150.0", report)
    self.assertIn("Education: 200.0", report)



if __name__ == "__main__":
    unittest.main()

```