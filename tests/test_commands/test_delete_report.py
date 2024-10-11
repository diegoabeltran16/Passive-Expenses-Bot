import unittest
from unittest.mock import patch, AsyncMock
import discord
from discord.ext import commands
from src.commands.delete_report import DeleteReport
from src.utils.lang import translate

class TestDeleteReportCommand(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.cog = DeleteReport(self.bot)
        self.ctx = AsyncMock()
        self.ctx.author.id = 1
        await self.bot.add_cog(self.cog)

    @patch('src.commands.delete_report.db_delete_report')
    @patch('src.commands.delete_report.delete_file')
    async def test_delete_report_success(self, mock_delete_file, mock_db_delete_report):
        # Mock the database and file deletion functions
        mock_db_delete_report.return_value = 'reports/1_report.pdf'
        mock_delete_file.return_value = True

        await self.cog.delete_report(self.ctx, report_id=1)

        # Ensure the response is as expected
        self.ctx.send.assert_called_once_with(translate('report_deleted_confirmation', 'en', id=1))

    @patch('src.commands.delete_report.db_delete_report', side_effect=Exception("Database error"))
    async def test_delete_report_error(self, mock_db_delete_report):
        await self.cog.delete_report(self.ctx, report_id=1)

        # Ensure the error message matches
        self.ctx.send.assert_called_once_with(translate('error_deleting_report', 'en', error="Database error"))

    @patch('src.commands.delete_report.db_delete_report', return_value=None)
    async def test_delete_report_not_found(self, mock_db_delete_report):
        await self.cog.delete_report(self.ctx, report_id=999)

        # Ensure the "not found" message is as expected
        self.ctx.send.assert_called_once_with(translate('no_report_found', 'en', id=999))

if __name__ == '__main__':
    unittest.main()
