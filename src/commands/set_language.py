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

    @commands.command(name='set_language', aliases=['ajustar_gasto'])
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
