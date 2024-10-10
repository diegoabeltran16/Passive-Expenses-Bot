import unittest
import sys
import os
import sqlite3
import discord
from unittest.mock import MagicMock, AsyncMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from commands.list_expenses import ListExpenses
from utils.lang import translate
from utils.shared import user_language
from utils.db import create_expenses_table

class TestListExpenses(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up a test bot and list expenses cog before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.list_expenses_cog = ListExpenses(self.bot)
        await self.bot.add_cog(self.list_expenses_cog)
        self.ctx = MagicMock()
        self.ctx.author.id = 1
        self.ctx.send = AsyncMock()

        # Set up an in-memory database for testing
        self.mock_conn = sqlite3.connect(':memory:')
        
        # Create the expenses table in the in-memory database
        create_expenses_table(self.mock_conn)

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.mock_conn.close()

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_list_expenses_no_expenses(self, mock_user_language):
        """
        Test listing expenses when no expenses are found.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Ensure the database has no expenses
        cursor = self.mock_conn.cursor()
        cursor.execute("DELETE FROM expenses")
        self.mock_conn.commit()

        # Call the command to list expenses when there are no expenses
        await self.list_expenses_cog.list_expenses(self.ctx, conn=self.mock_conn)

        # Check if the response was sent correctly
        expected_message = translate("no_expenses_found", language="en")
        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_list_expenses_with_expenses(self, mock_user_language):
        """
        Test listing expenses when expenses are present.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Insert a mock expense into the database
        cursor = self.mock_conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (user_id, amount, description, category, date_added)
            VALUES (?, ?, ?, ?, datetime('now'))
        ''', (1, 50.0, "Grocery shopping", "Groceries"))
        self.mock_conn.commit()

        # Fetch the date_added for the expense to construct the expected message dynamically
        cursor.execute("SELECT id, amount, description, date_added FROM expenses WHERE user_id = ?", (1,))
        expense = cursor.fetchone()
        expense_id, amount, description, date_added = expense

        # Call the command to list expenses
        await self.list_expenses_cog.list_expenses(self.ctx, conn=self.mock_conn)

        # Construct the expected message dynamically
        expected_message = translate("here_are_your_expenses", language="en") + "\n"
        expected_message += f"ID: {expense_id}, Amount: {amount}, Description: {description}, Date Added: {date_added}\n"

        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_list_expenses_db_error(self, mock_user_language):
        """
        Test listing expenses when the database connection fails.
        """
        mock_user_language[1] = "en"

        # Simulate a database connection failure by setting side_effect
        with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("Unable to connect to the database")):
            # Call the command to list expenses
            await self.list_expenses_cog.list_expenses(self.ctx)

            # Check if the error message was sent
            self.ctx.send.assert_called_with("Could not open the database. Please try again later.")

if __name__ == '__main__':
    unittest.main()
