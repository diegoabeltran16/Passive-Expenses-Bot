# src/commands/set_language.py

from discord.ext import commands
from src.utils.lang import translate
from src.utils.shared import user_language
from src.utils.db import connect_db

class SetLanguage(commands.Cog):
    """
    A Cog that allows users to set their preferred language for the bot.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setlanguage')
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

        # Optionally, persist language preferences in the database
        self._update_language_in_db(user_id, language)

        # Provide feedback in the user's new preferred language
        response = translate("language_set", language=language, language_value=language)
        await ctx.send(response)

    def _update_language_in_db(self, user_id, language):
        """
        Updates the user's preferred language in the database (optional persistence).
        """
        conn = connect_db()
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
        conn.close()

async def setup(bot):
    await bot.add_cog(SetLanguage(bot))
