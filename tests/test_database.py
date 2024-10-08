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
