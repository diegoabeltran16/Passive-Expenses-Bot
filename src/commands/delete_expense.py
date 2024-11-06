import os
import sqlite3
import logging
from discord.ext import commands
from src.utils.lang import translate  # Import the translation module for multilingual responses
from src.utils import db  # Import the db module where database functions are located.
from src.utils.shared import get_user_language  # Import the function to get user language from the database
import yaml

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load configuration from config.yaml
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        db.create_tables(conn)  # Call a consolidated function to create all necessary tables
        conn.close()

# Define a Cog class to handle the "delete_expense" command.
class DeleteExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_expense', aliases=['eliminar_gasto'])
    async def delete_expense(self, ctx, expense_id: int):
        """
        A command that deletes an expense from the SQLite database.
        """
        # Get the user's preferred language from the database or default to 'en'
        user_id = ctx.author.id
        language = get_user_language(user_id) or "en"  # Default to "en" if language is not set

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
                # Check if the expense exists
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM expenses WHERE id = ?", (expense_id,))
                if cursor.fetchone() is None:
                    response = translate("no_expense_found", language, id=expense_id)
                    await ctx.send(response)
                    return

                # Delete the expense using the provided ID
                db.delete_expense(conn, expense_id)

                # Use the translation function to generate a response in the user's language
                response = translate("expense_deleted", language, id=expense_id)

                # Send the translated response to the Discord channel
                await ctx.send(response)

        except sqlite3.OperationalError as e:
            logging.error(f"Error: {e}")
            await ctx.send(translate("error_connecting_db", language))

# Asynchronous function to add the Cog to the bot.
async def setup(bot):
    await bot.add_cog(DeleteExpense(bot))
