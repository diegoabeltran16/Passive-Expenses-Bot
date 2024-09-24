# Import necessary modules from discord.ext for creating commands
from discord.ext import commands
from utils.shared import user_language  # Correctly import the shared user_language dictionary

class SetLanguage(commands.Cog):
    """
    A Cog that allows users to set their preferred language for the bot's responses.
    """
    
    def __init__(self, bot):
        """
        Constructor that initializes the bot instance.
        """
        self.bot = bot

    @commands.command(name='set_language')
    async def set_language(self, ctx, language_code: str):
        """
        Command to set the preferred language for the user.
        """
        if language_code not in ["en", "es"]:
            await ctx.send("Unsupported language. Available options: en, es")
            return

        # Store user's language preference
        user_language[ctx.author.id] = language_code  # Update the shared dictionary
        print(f"User {ctx.author.id} set language to {language_code}")
        
        # Debugging statement to confirm language setting
        print(f"user_language dictionary after update: {user_language}")
        
        await ctx.send(f"Language set to {language_code}.")

# Asynchronous setup function to add the Cog to the bot
async def setup(bot):
    if not bot.get_cog("SetLanguage"):
        await bot.add_cog(SetLanguage(bot))
        print("SetLanguage Cog loaded successfully")
    else:
        print("SetLanguage Cog already loaded, skipping.")

# Debugging statement to verify that we're using the shared user_language
print(f"user_language dictionary after importing shared module: {user_language}")
