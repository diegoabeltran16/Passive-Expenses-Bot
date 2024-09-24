# Import necessary modules
from discord.ext import commands
from utils.lang import translate  # Import translation functionality
from utils import db  # Import database functions
from utils.shared import user_language

import yaml


# Load configuration from config.yaml
with open("config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Define a Cog class to handle the "log_expense" command
class LogExpense(commands.Cog):
    """
    A Cog that manages the logging of expenses into the SQLite database.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, description: str):
        """
        Command to log a new expense into the SQLite database.
        """
        # Retrieve the user's preferred language or default to English
        user_id = ctx.author.id
        language = user_language.get(ctx.author.id, config.get("default_language", "en"))

        # Debug print to confirm language retrieval
        print(f"User {user_id} is using language: {language}")

        # Add the expense to the SQLite database
        expense_id = db.add_expense(amount, description)

        # Use the translation function to generate a response in the appropriate language
        response = translate("expense_logged", language, id=expense_id, amount=amount, description=description)

        # Confirm that the expense has been logged by sending a message to the Discord channel
        await ctx.send(response)

# Asynchronous setup function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(LogExpense(bot))
