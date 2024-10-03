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
