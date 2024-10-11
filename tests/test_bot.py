import unittest
import sys
import os
import discord
from unittest.mock import AsyncMock, MagicMock, patch
from discord.ext import commands

# Ensure the src directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Correct the import based on the project structure
from src.bot import bot, load_extensions
from src.config.config import get_config


class TestBot(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up the bot instance before each test.
        """
        prefix = get_config('bot.prefix', '!')
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=prefix, intents=intents)

        # Patch the bot's login process to mock the user attribute indirectly
        self.user_mock = MagicMock()
        self.user_mock.id = 12345
        self.user_mock.name = "MockBot"
        
        # Mock the bot's user property correctly
        self.bot._user = self.user_mock

        # Unload all extensions to avoid double loading
        for ext in list(self.bot.extensions):
            await self.bot.unload_extension(ext)

        # Load extensions only once for testing
        await load_extensions()

        # Mock the send method for ctx
        self.ctx = MagicMock()
        self.ctx.send = AsyncMock()
        self.ctx.author.id = 1
        self.ctx.message = MagicMock()
        self.ctx.message.content = "!ping"
        self.ctx.message.author = self.ctx.author

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        await self.bot.close()

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
        # Unload any currently loaded extensions before testing
        for ext in list(self.bot.extensions):
            await self.bot.unload_extension(ext)

        with patch.object(self.bot, 'load_extension', new_callable=AsyncMock) as mock_load_extension:
            await load_extensions()
            extensions = [
                'src.commands.log_expense',
                'src.commands.delete_expense',
                'src.commands.list_expenses',
                'src.commands.update_expense',
                'src.commands.set_language',
                'src.commands.log_report',
                'src.commands.get_reports',
                'src.commands.delete_report'
            ]
            for ext in extensions:
                mock_load_extension.assert_any_call(ext)

            # Ensure the extensions were loaded exactly as expected
            self.assertEqual(mock_load_extension.call_count, len(extensions))

    async def test_command_invocation(self):
        """
        Test invoking a non-existent command to ensure proper handling.
        """
        # Mock the bot's user properly before testing
        self.bot._user = self.user_mock

        # Create a fake message object for a non-existent command
        message = self.ctx.message
        message.content = "!nonexistent_command"
        ctx = await self.bot.get_context(message)
        
        # Invoke the command and simulate command error handling
        with patch.object(self.bot, 'dispatch') as mock_dispatch:
            await self.bot.invoke(ctx)
            mock_dispatch.assert_called_with('command_error', ctx, unittest.mock.ANY)

        # Verify that the bot doesn't call ctx.send() because the command doesn't exist
        self.ctx.send.assert_not_called()


if __name__ == '__main__':
    unittest.main()
