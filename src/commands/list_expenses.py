import os
import sqlite3
import logging
from discord.ext import commands
from src.utils.lang import translate
from src.utils.db import list_expenses as fetch_expenses
from src.utils.shared import get_user_language
import yaml

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Load configuration from config.yaml
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Create the expenses table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                description TEXT NOT NULL,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

class ListExpenses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='list_expenses', aliases=['listar_gastos'])
    async def list_expenses(self, ctx):
        """
        A command that lists all expenses from the SQLite database and sends them to the Discord channel.
        """
        user_id = ctx.author.id
        language = get_user_language(user_id)
        logging.debug(f"User {user_id} requested expense listing in language '{language}'.")

        # Database path and initialization
        db_directory = os.path.join(os.path.dirname(__file__), "../database")
        db_path = os.path.join(db_directory, "expenses.db")
        
        # Ensure the database and directory exist
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)
        
        initialize_database(db_path)
        logging.debug("Database initialized and connection path set.")

        try:
            # Open database connection
            conn = sqlite3.connect(db_path)
            logging.debug("Database connection opened.")

            # Fetch expenses for the user
            expenses = fetch_expenses(conn, user_id)
            conn.close()  # Close the connection after fetching data
            logging.debug(f"Fetched expenses: {expenses}")

            # Handle response based on whether expenses were found
            if not expenses:
                response = translate("no_expenses_found", language)
            else:
                response = translate("here_are_your_expenses", language) + "\n"
                for expense in expenses:
                    response += f"ID: {expense[0]}, Amount: {expense[1]}, Description: {expense[2]}, Date Added: {expense[3]}\n"

            # Send the response to the Discord channel
            await ctx.send(response)

        except AttributeError as e:
            logging.error(f"Function not found in db module: {e}")
            await ctx.send("Error: Function not found in database utilities.")
        
        except sqlite3.OperationalError as e:
            logging.error(f"Error querying database: {e}")
            await ctx.send(translate("error_connecting_db", language, error=str(e)))

# Async function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(ListExpenses(bot))
