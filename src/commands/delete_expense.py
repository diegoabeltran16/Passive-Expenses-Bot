import os
import sqlite3
from discord.ext import commands
from src.utils.lang import translate  # Import the translation module for multilingual responses
from src.utils import db  # Import the db module where database functions are located.
from src.utils.shared import user_language  # Import user_language dictionary to access user language preferences
import yaml

# Load configuration from config.yaml
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        db.create_expenses_table(conn)  # Ensure the table is created
        conn.close()

# Define a Cog class to handle the "delete_expense" command.
class DeleteExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_expense')
    async def delete_expense(self, ctx, expense_id: int):
        """
        A command that deletes an expense from the SQLite database.
        """
        # Get the user's preferred language, defaulting to 'en' if not set
        user_id = ctx.author.id
        language = user_language.get(user_id, config.get("default_language", "en"))

        # Generate an absolute path to the database
        db_directory = os.path.join(os.path.dirname(__file__), "../database")
        db_path = os.path.join(db_directory, "expenses.db")

        # Ensure the directory exists
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)

        # Initialize the database if needed
        initialize_database(db_path)

        # Connect to the database and delete the expense
        try:
            with sqlite3.connect(db_path) as conn:
                db.delete_expense(conn, expense_id)

                # Use the translation function to generate a response in the user's language
                response = translate("expense_deleted", language, id=expense_id)

                # Send the translated response to the Discord channel
                await ctx.send(response)

        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
            await ctx.send("Could not open the database. Please try again later.")

# Asynchronous function to add the Cog to the bot.
async def setup(bot):
    await bot.add_cog(DeleteExpense(bot))
