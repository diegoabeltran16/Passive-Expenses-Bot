import unittest
import sys
import os
import sqlite3
import discord
from unittest.mock import MagicMock, AsyncMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from commands.log_expense import LogExpense
from utils.lang import translate
from utils.shared import user_language

class TestLogExpense(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up a test bot and log expense cog before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.log_expense_cog = LogExpense(self.bot)
        await self.bot.add_cog(self.log_expense_cog)
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
        from utils.db import create_expenses_table
        create_expenses_table(self.mock_conn)

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.mock_conn.close()
        self.conn_patcher.stop()

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_log_expense_success(self, mock_user_language):
        """
        Test logging an expense successfully.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Call the command to log an expense
        await self.log_expense_cog.log_expense(self.ctx, 100.0, description="Lunch at cafe", conn=self.mock_conn)

        # Check if the response was sent correctly
        expected_message = translate("expense_logged", language="en", id=1, amount=100.0, description="Lunch at cafe")
        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_log_expense_error(self, mock_user_language):
        """
        Test logging an expense when the database connection fails.
        """
        mock_user_language[1] = "en"

        # Simulate a database connection failure by setting side_effect
        with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("Unable to connect to the database")):
            # Call the command to log an expense
            await self.log_expense_cog.log_expense(self.ctx, 100.0, description="Lunch at cafe")

            # Check if the error message was sent
            self.ctx.send.assert_called_with("Could not open the database. Please try again later.")

if __name__ == '__main__':
    unittest.main()
