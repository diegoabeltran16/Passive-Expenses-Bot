import unittest
import sys
import os
import sqlite3
import discord
from unittest.mock import MagicMock, AsyncMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from commands.delete_expense import DeleteExpense
from utils.lang import translate
from utils.shared import user_language

class TestDeleteExpense(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up a test bot and delete expense cog before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.delete_expense_cog = DeleteExpense(self.bot)
        await self.bot.add_cog(self.delete_expense_cog)
        self.ctx = MagicMock()
        self.ctx.author.id = 1
        self.ctx.send = AsyncMock()

        # Patch the connect_db method in the db module
        self.conn_patcher = patch('utils.db.connect_db')
        self.mock_connect_db = self.conn_patcher.start()

        # Set up an in-memory database for testing
        self.mock_conn = sqlite3.connect(':memory:')
        self.mock_connect_db.return_value = self.mock_conn

        # Import and create the expenses table in the in-memory database
        from utils.db import create_expenses_table, insert_expense
        create_expenses_table(self.mock_conn)

        # Insert an expense to delete in the test
        self.expense_id = insert_expense(self.mock_conn, user_id=1, amount=100.0, description="Test expense")

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.mock_conn.close()
        self.conn_patcher.stop()

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_delete_expense_success(self, mock_user_language):
        """
        Test deleting an expense successfully.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Call the command to delete an expense
        await self.delete_expense_cog.delete_expense(self.ctx, self.expense_id)

        # Check if the response was sent correctly
        expected_message = translate("expense_deleted", language="en", id=self.expense_id)
        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_delete_expense_error(self, mock_user_language):
        """
        Test deleting an expense when the database connection fails.
        """
        mock_user_language[1] = "en"

        # Simulate a database connection failure by setting side_effect
        with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("Unable to connect to the database")):
            # Call the command to delete an expense
            await self.delete_expense_cog.delete_expense(self.ctx, self.expense_id)

            # Check if the error message was sent
            self.ctx.send.assert_called_with("Could not open the database. Please try again later.")

if __name__ == '__main__':
    unittest.main()
