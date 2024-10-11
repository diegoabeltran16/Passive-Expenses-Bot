# tests/test_commands/test_list_reports.py

import unittest
from unittest.mock import AsyncMock, patch
from discord.ext import commands
import discord
from src.commands.list_reports import ListReports

class TestListReportsCommand(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.cog = ListReports(self.bot)
        await self.bot.add_cog(self.cog)

        self.ctx = AsyncMock()
        self.ctx.author.id = 1

    @patch('src.commands.list_reports.get_reports_by_user')
    @patch('src.commands.list_reports.get_user_language', return_value='en')
    async def test_list_reports_with_reports(self, mock_get_language, mock_get_reports):
        mock_get_reports.return_value = [
            {'report_id': 1, 'file_path': 'reports/1_report.pdf'},
            {'report_id': 2, 'file_path': 'reports/2_report.csv'}
        ]

        await self.cog.list_reports(self.ctx)
        self.ctx.send.assert_called_with("Your reports:\nID: 1, File Path: reports/1_report.pdf\nID: 2, File Path: reports/2_report.csv")

    @patch('src.commands.list_reports.get_reports_by_user', return_value=[])
    @patch('src.commands.list_reports.get_user_language', return_value='en')
    async def test_list_reports_no_reports(self, mock_get_language, mock_get_reports):
        await self.cog.list_reports(self.ctx)
        self.ctx.send.assert_called_with("You have no reports.")

    @patch('src.commands.list_reports.get_reports_by_user', side_effect=Exception("Database error"))
    @patch('src.commands.list_reports.get_user_language', return_value='en')
    async def test_list_reports_error(self, mock_get_language, mock_get_reports):
        await self.cog.list_reports(self.ctx)
        self.ctx.send.assert_called_with("Failed to retrieve reports: Database error")

if __name__ == '__main__':
    unittest.main()
