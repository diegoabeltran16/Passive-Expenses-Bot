import os
import sqlite3
from discord.ext import commands
from src.utils.lang import translate
from src.utils import db
from src.utils.shared import user_language
import yaml

# Load configuration from config.yaml
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        db.create_expenses_table(conn)
        conn.close()

class ListExpenses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='list_expenses')
    async def list_expenses(self, ctx, conn=None):
        """
        A command that lists all expenses from the SQLite database and sends them to the Discord channel.
        Parameters:
        ctx: The context of the command invocation.
        conn: Optional database connection for testing.
        """
        user_id = ctx.author.id
        language = user_language.get(user_id, config.get("default_language", "en"))

        if not conn:
            # Generate an absolute path to the database
            db_directory = os.path.join(os.path.dirname(__file__), "../database")
            db_path = os.path.join(db_directory, "expenses.db")

            # Ensure the directory exists
            if not os.path.exists(db_directory):
                os.makedirs(db_directory)

            # Initialize the database if needed
            initialize_database(db_path)

            try:
                conn = sqlite3.connect(db_path)
            except sqlite3.OperationalError as e:
                print(f"Error: {e}")
                await ctx.send("Could not open the database. Please try again later.")
                return

        try:
            expenses = db.list_expenses(conn, user_id)

            if not expenses:
                response = translate("no_expenses_found", language)
            else:
                response = translate("here_are_your_expenses", language) + "\n"
                for expense in expenses:
                    response += f"ID: {expense[0]}, Amount: {expense[2]}, Description: {expense[3]}, Date Added: {expense[5]}\n"

            await ctx.send(response)

        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
            await ctx.send("Could not open the database. Please try again later.")

# Async function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(ListExpenses(bot))
