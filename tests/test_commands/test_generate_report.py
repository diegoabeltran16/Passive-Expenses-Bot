# tests/test_commands/test_generate_report.py

import unittest
from unittest.mock import patch, AsyncMock
import discord
from discord.ext import commands
from src.commands.generate_report import GenerateReport
from src.utils.shared import set_user_language
import os

class TestGenerateReportCommand(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
        self.cog = GenerateReport(self.bot)
        await self.bot.add_cog(self.cog)

        self.ctx = AsyncMock()
        self.ctx.author.id = 1
        set_user_language(self.ctx.author.id, 'en')  # Set the language for testing

    @patch('src.commands.generate_report.generate_report')
    @patch('src.commands.generate_report.connect_db')
    async def test_generate_report_text(self, mock_connect_db, mock_generate_report):
        mock_conn = AsyncMock()  # Mock the connection
        mock_connect_db.return_value = mock_conn
        mock_generate_report.return_value = "Report generated successfully."

        await self.cog.generate_report(self.ctx, 'text', None, None, None)

        expected_message = "Text report generated successfully.\nReport generated successfully."
        self.ctx.send.assert_called_with(expected_message)

    @patch('src.commands.generate_report.generate_report')
    @patch('src.commands.generate_report.connect_db')
    async def test_generate_report_pdf(self, mock_connect_db, mock_generate_report):
        mock_conn = AsyncMock()
        mock_connect_db.return_value = mock_conn
        mock_generate_report.return_value = b'%PDF-1.4...'

        # Patch save_file to return a consistent path, normalized with os.path.join for cross-platform compatibility
        with patch('src.utils.file_manager.save_file', return_value=os.path.join("reports", "1_report.pdf")):
            await self.cog.generate_report(self.ctx, 'pdf', None, None, None)

        # Use os.path.join for the expected path to ensure consistency with the actual value
        expected_file_path = os.path.join("reports", "1_report.pdf")
        expected_message = f"PDF report generated: {expected_file_path}"
        self.ctx.send.assert_called_with(expected_message)

    @patch('src.commands.generate_report.generate_report', side_effect=ValueError("Error generating report"))
    @patch('src.commands.generate_report.connect_db')
    async def test_generate_report_failure(self, mock_connect_db, mock_generate_report):
        mock_conn = AsyncMock()
        mock_connect_db.return_value = mock_conn

        await self.cog.generate_report(self.ctx, 'pdf', None, None, None)

        self.ctx.send.assert_called_with("Failed to generate report: Error generating report")

if __name__ == '__main__':
    unittest.main()
