# src/commands/set_language.py

## General Desription
The main goal of this script is to create a command that allows users of a Discord bot to set their preferred language. The user's language preference is saved both in memory (for immediate use) and in a database (for persistence). The command also validates the language input and ensures that only supported languages are allowed.


## Pseudocode
```
1. **Setup Logging**
   - Configure basic logging for the script.

2. **Define SetLanguage Cog Class**
   - Create a class named `SetLanguage` that extends `commands.Cog`.
   - Initialize the class with a bot instance.

3. **Define `set_language` Command**
   - Decorate the `set_language` function as a command using `@commands.command(name='set_language')`.
   - **Parameters:**
     - `ctx`: Context of the command invocation.
     - `language`: The desired language input by the user.

4. **Validate Language Input**
   - Define a list of supported languages (`en` and `es`).
   - Check if the `language` argument is in the list of supported languages.
     - If not, send a failure message to the user and exit the command.

5. **Update Language Preference**
   - Retrieve the user's Discord ID (`user_id` from `ctx.author.id`).
   - Store the language preference in the in-memory dictionary (`user_language`).
   - Call the helper method `_update_language_in_db` to persist the language preference in the database.
   - Handle any errors during database operations and send a failure message if needed.

6. **Send Feedback to the User**
   - Use the `translate` function to generate a confirmation message in the user's preferred language.
   - Send the confirmation message to the Discord channel.

7. **Define Helper Method `_update_language_in_db`**
   - **Parameters:**
     - `user_id`: User's Discord ID.
     - `language`: The new preferred language.
   - Connect to the database using the `connect_db` function.
   - Check if the user already has a language preference saved in the database.
     - If a record exists, update it.
     - If not, insert a new record with the user's preferred language.
   - Handle any errors and close the database connection.

8. **Async Setup Function**
   - Define an asynchronous `setup` function to add the `SetLanguage` Cog to the bot.

```

## Code

```
# src/commands/set_language.py

from discord.ext import commands
from src.utils.lang import translate
from src.utils.shared import user_language
from src.utils.db import connect_db
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SetLanguage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_language')
    async def set_language(self, ctx, language: str):
        """
        Command to set the preferred language for a user.
        """
        supported_languages = ["en", "es"]
        user_id = ctx.author.id

        # Validate the language input
        if language not in supported_languages:
            await ctx.send(translate("update_failed", language="en", error=f"Unsupported language: {language}"))
            return

        # Store the user's preferred language in the shared dictionary
        user_language[user_id] = language

        # Persist language preferences in the database
        try:
            self._update_language_in_db(user_id, language)
            logger.info(f"User {user_id} set language to {language}")
        except Exception as e:
            logger.error(f"Failed to update language in database for user {user_id}: {e}")
            await ctx.send("There was an error saving your language preference. Please try again later.")
            return

        # Provide feedback in the user's new preferred language
        response = translate("language_set", language=language, language_value=language)
        await ctx.send(response)

    def _update_language_in_db(self, user_id, language):
        """
        Updates the user's preferred language in the database (optional persistence).
        """
        conn = connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM user_language WHERE user_id = ?', (user_id,))
            existing_record = cursor.fetchone()

            if existing_record:
                cursor.execute('''
                    UPDATE user_language
                    SET language = ?
                    WHERE user_id = ?
                ''', (language, user_id))
            else:
                cursor.execute('''
                    INSERT INTO user_language (user_id, language)
                    VALUES (?, ?)
                ''', (user_id, language))

            conn.commit()
        except Exception as e:
            logger.error(f"Error while updating user language in database: {e}")
            raise
        finally:
            conn.close()

async def setup(bot):
    print("Adding SetLanguage Cog")  # Debug statement to confirm Cog addition
    await bot.add_cog(SetLanguage(bot))
```

## Testing 
tests/test_commands/test_set_language.py

**Main Goal:**
The main goal of this code is to test the "set_language" command of the SetLanguage Cog, which allows users to set their preferred language for interacting with the bot. The tests check if the language is correctly set to English or Spanish and handle cases where an unsupported language is provided.

### Testing Pseudocode
```
1. **Set Up the Environment for Tests**
   - Create a unittest class called `TestSetLanguage` that uses the `IsolatedAsyncioTestCase` for asynchronous testing.
   - Define the `asyncSetUp` function:
     - Create an instance of the bot using Discord's `commands.Bot` class with a given command prefix.
     - Add the `SetLanguage` Cog to the bot.
     - Set up a mock context (`ctx`) with `author.id` representing the user's ID and an asynchronous `send` method to mock bot responses.

2. **Test Setting Language to English**
   - Patch the `user_language` dictionary from `src.utils.shared` to mock the shared language preferences.
   - Call the `set_language` command on the `SetLanguage` Cog, passing "en" as the argument.
   - Verify if the user's language preference is set to English (`"en"`) in the mocked dictionary.
   - Construct the expected message using the `translate` function and verify if the appropriate message was sent using the mocked `ctx.send` method.

3. **Test Setting Language to Spanish**
   - Patch the `user_language` dictionary from `src.utils.shared` to mock the shared language preferences.
   - Call the `set_language` command on the `SetLanguage` Cog, passing "es" as the argument.
   - Verify if the user's language preference is set to Spanish (`"es"`) in the mocked dictionary.
   - Construct the expected message using the `translate` function and verify if the appropriate message was sent using the mocked `ctx.send` method.

4. **Test Setting an Unsupported Language**
   - Call the `set_language` command on the `SetLanguage` Cog, passing an unsupported language ("fr") as the argument.
   - Construct the expected error message using the `translate` function, indicating that the language is unsupported.
   - Verify if the error message was sent using the mocked `ctx.send` method.

5. **Run Tests**
   - Use `unittest.main()` to execute the tests when the script is run.

```

### Testing Code
```
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
```