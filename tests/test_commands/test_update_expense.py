import unittest
import sys
import os
import sqlite3
import discord
from unittest.mock import MagicMock, AsyncMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from commands.update_expense import UpdateExpense
from utils.lang import translate
from utils.shared import user_language
from utils.db import create_expenses_table

class TestUpdateExpense(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up a test bot and update expense cog before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.update_expense_cog = UpdateExpense(self.bot)
        await self.bot.add_cog(self.update_expense_cog)
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
    async def test_update_expense_success(self, mock_user_language):
        """
        Test updating an expense successfully.
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

        # Retrieve the inserted expense ID for updating
        cursor.execute("SELECT id FROM expenses WHERE user_id = ?", (1,))
        expense_id = cursor.fetchone()[0]

        # Call the command to update the expense
        await self.update_expense_cog.update_expense(self.ctx, expense_id, 100.0, new_description="Updated description")

        # Construct the expected response
        expected_message = translate("expense_updated", language="en", id=expense_id, amount=100.0, description="Updated description")

        # Check if the response was sent correctly
        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_update_expense_db_error(self, mock_user_language):
        """
        Test updating an expense when the database connection fails.
        """
        mock_user_language[1] = "en"

        # Simulate a database connection failure by setting side_effect
        with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("Unable to connect to the database")):
            # Call the command to update an expense
            await self.update_expense_cog.update_expense(self.ctx, 1, 100.0, new_description="Should fail")

            # Check if the error message was sent
            self.ctx.send.assert_called_with("Could not open the database. Please try again later.")

if __name__ == '__main__':
    unittest.main()
