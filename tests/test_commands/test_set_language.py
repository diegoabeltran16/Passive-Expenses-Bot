import unittest
import sys
import os
import discord
from unittest.mock import MagicMock, AsyncMock, patch

# Add the correct path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.commands.set_language import SetLanguage
from src.utils.lang import translate
from discord.ext import commands

class TestSetLanguage(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """Set up a test bot and language cog."""
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.set_language_cog = SetLanguage(self.bot)
        await self.bot.add_cog(self.set_language_cog)
        self.ctx = MagicMock()
        self.ctx.author.id = 1
        self.ctx.send = AsyncMock()

    @patch('src.utils.shared.user_language', new_callable=dict)
    async def test_set_language_to_english(self, mock_user_language):
        """Test setting language to English."""
        # Call the command to set the language to English
        await self.set_language_cog.set_language(self.ctx, "en")

        # Verify that the user language has been set correctly
        mock_user_language[self.ctx.author.id] = "en"  # Update the mocked dictionary
        self.assertEqual(mock_user_language[self.ctx.author.id], "en")

        # Check that the appropriate message was sent
        expected_message = translate("language_set", language="en", language_value="en")
        self.ctx.send.assert_called_with(expected_message)

    @patch('src.utils.shared.user_language', new_callable=dict)
    async def test_set_language_to_spanish(self, mock_user_language):
        """Test setting language to Spanish."""
        # Call the command to set the language to Spanish
        await self.set_language_cog.set_language(self.ctx, "es")

        # Verify that the user language has been set correctly
        mock_user_language[self.ctx.author.id] = "es"  # Update the mocked dictionary
        self.assertEqual(mock_user_language[self.ctx.author.id], "es")

        # Check that the appropriate message was sent
        expected_message = translate("language_set", language="es", language_value="es")
        self.ctx.send.assert_called_with(expected_message)

    async def test_invalid_language(self):
        """Test setting an unsupported language."""
        await self.set_language_cog.set_language(self.ctx, "fr")
        expected_message = translate("update_failed", language="en", error="Unsupported language: fr")
        self.ctx.send.assert_called_with(expected_message)

if __name__ == '__main__':
    unittest.main()
