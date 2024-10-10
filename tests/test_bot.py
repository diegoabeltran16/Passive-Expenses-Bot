import unittest
import sys
import os
import discord
from unittest.mock import AsyncMock, MagicMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bot import bot, load_extensions

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
        self.ctx.message.content = "!ping"
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
            # Override bot instance in load_extensions function for testing
            await load_extensions()  # Call the method to load extensions

            # Check that extensions were attempted to be loaded
            extensions = [
                'src.commands.log_expense',
                'src.commands.delete_expense',
                'src.commands.list_expenses',
                'src.commands.update_expense',
                'src.commands.set_language'
            ]
            for ext in extensions:
                mock_load_extension.assert_any_call(ext)

    async def test_command_invocation(self):
        """
        Test invoking a non-existent command to ensure proper handling.
        """
        # Create a fake message object for a non-existent command
        self.ctx.message.content = "!nonexistent_command"
        message = self.ctx.message
        ctx = await self.bot.get_context(message)

        # Invoke the non-existent command
        await self.bot.invoke(ctx)

        # Verify that the bot doesn't call ctx.send() because the command doesn't exist
        self.ctx.send.assert_not_called()

if __name__ == '__main__':
    unittest.main()
