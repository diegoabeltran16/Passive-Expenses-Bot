# src/commands/set_language.py

from discord.ext import commands
from src.utils.lang import translate
from src.utils.shared import get_user_language, set_user_language
from src.utils.db import connect_db
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SetLanguage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_language', aliases=['ajustar_idioma'])
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

        # Persist language preferences in the database
        try:
            # Use the set_user_language function to store language preference in the database
            set_user_language(user_id, language)
            logger.info(f"User {user_id} set language to {language}")
        except Exception as e:
            logger.error(f"Failed to update language in database for user {user_id}: {e}")
            await ctx.send("There was an error saving your language preference. Please try again later.")
            return

        # Provide feedback in the user's new preferred language
        response = translate("language_set", language=language, language_value=language)
        await ctx.send(response)

async def setup(bot):
    print("Adding SetLanguage Cog")  # Debug statement to confirm Cog addition
    await bot.add_cog(SetLanguage(bot))
