import unittest
import sys
import os
import discord
from unittest.mock import AsyncMock, MagicMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bot import bot, load_extensions
from src.utils.db import insert_report, get_reports_by_user, delete_report

class TestBot(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up the bot instance before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)

        # Patch the run method to prevent the bot from actually running during tests
        self.run_patcher = patch.object(self.bot, 'run', return_value=None)
        self.mock_run = self.run_patcher.start()

        # Mock the bot's user object to simulate the bot being logged in
        self.bot.user = MagicMock()
        self.bot.user.id = 12345  # Set a mock bot user ID

        # Mock the send method for ctx
        self.ctx = MagicMock()
        self.ctx.send = AsyncMock()
        self.ctx.author.id = 1
        self.ctx.message = MagicMock()
        self.ctx.message.author = self.ctx.author

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.run_patcher.stop()

    async def test_ping_command(self):
        """
        Test the ping command.
        """
        @self.bot.command(name='ping')
        async def ping(ctx):
            await ctx.send("Pong!")

        # Get the command object and invoke it directly
        command = self.bot.get_command('ping')
        await command(self.ctx)
        
        # Assert that the bot sends the "Pong!" message
        self.ctx.send.assert_called_with("Pong!")

    async def test_load_extensions(self):
        """
        Test loading extensions dynamically.
        """
        # Patch the bot's load_extension method
        with patch.object(self.bot, 'load_extension', new_callable=AsyncMock) as mock_load_extension:
            await load_extensions()  # Call the method to load extensions

            # Check that extensions were attempted to be loaded
            extensions = [
                'src.commands.log_expense',
                'src.commands.delete_expense',
                'src.commands.list_expenses',
                'src.commands.update_expense',
                'src.commands.set_language',
                'src.commands.log_report',     # Added new command for log report
                'src.commands.get_reports',    # Added new command for get reports
                'src.commands.delete_report'   # Added new command for delete report
            ]
            for ext in extensions:
                mock_load_extension.assert_any_call(ext)

    async def test_log_report_command(self):
        """
        Test the log_report command to verify it logs a report correctly.
        """
        # Simulate the log_report command
        @self.bot.command(name='log_report')
        async def log_report(ctx, report_name, file_path):
            # Mock inserting a report into the database
            report_id = insert_report(MagicMock(), ctx.author.id, report_name, file_path)
            if report_id:
                await ctx.send(f"Report logged successfully with ID {report_id}.")
            else:
                await ctx.send("Error logging report.")

        self.ctx.message.content = "!log_report 'Monthly Report' '/path/to/report.pdf'"
        command = self.bot.get_command('log_report')
        await command(self.ctx, 'Monthly Report', '/path/to/report.pdf')
        self.ctx.send.assert_called_with("Report logged successfully with ID 1.")

    async def test_get_reports_command(self):
        """
        Test the get_reports command to ensure it fetches reports for a user.
        """
        @self.bot.command(name='get_reports')
        async def get_reports(ctx):
            reports = get_reports_by_user(MagicMock(), ctx.author.id)
            if reports:
                await ctx.send(f"Retrieved {len(reports)} reports.")
            else:
                await ctx.send("No reports found.")

        self.ctx.message.content = "!get_reports"
        command = self.bot.get_command('get_reports')
        await command(self.ctx)
        self.ctx.send.assert_called_with("Retrieved 1 reports.")

    async def test_delete_report_command(self):
        """
        Test the delete_report command to ensure it deletes a report by ID.
        """
        @self.bot.command(name='delete_report')
        async def delete_report(ctx, report_id):
            delete_report(MagicMock(), report_id)
            await ctx.send(f"Report with ID {report_id} deleted.")

        self.ctx.message.content = "!delete_report 1"
        command = self.bot.get_command('delete_report')
        await command(self.ctx, 1)
        self.ctx.send.assert_called_with("Report with ID 1 deleted.")

if __name__ == '__main__':
    unittest.main()
