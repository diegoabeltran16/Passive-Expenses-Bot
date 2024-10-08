import os
import sqlite3
import logging
from discord.ext import commands
from src.utils.lang import translate
from src.utils.shared import user_language
from src.utils.db import insert_expense, create_expenses_table
import yaml

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load configuration from config.yaml
with open("src/config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        create_expenses_table(conn)  # Ensure the table is created
        conn.close()

# Define a Cog class to handle the "log_expense" command
class LogExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, *, description: commands.clean_content, conn=None):
        """
        Command to log a new expense into the SQLite database.
        
        Parameters:
        ctx: The context of the command invocation.
        amount: The amount spent.
        description: The description of the expense.
        conn: Optional database connection for testing.
        """
        # Retrieve user's preferred language or use default
        user_id = ctx.author.id
        language = user_language.get(ctx.author.id, config.get("default_language", "en"))

        # Log language confirmation
        logging.info(f"User {user_id} is using language: {language}")

        # Use the provided database connection or create a new one if none is provided (for testing)
        try:
            if not conn:
                # Generate an absolute path to the database
                db_directory = os.path.join(os.path.dirname(__file__), "../database")
                db_path = os.path.join(db_directory, "expenses.db")

                # Ensure the directory exists
                if not os.path.exists(db_directory):
                    os.makedirs(db_directory)

                # Initialize the database if needed
                initialize_database(db_path)

                # Create the connection
                conn = sqlite3.connect(db_path)

            # Add the expense to the database
            expense_id = insert_expense(conn, user_id, amount, description)

            # Generate a response in the appropriate language
            response = translate("expense_logged", language, id=expense_id, amount=amount, description=description)

            # Send confirmation message to Discord channel
            await ctx.send(response)
        
        except sqlite3.OperationalError as e:
            logging.error(f"Error: {e}")
            await ctx.send("Could not open the database. Please try again later.")
        finally:
            if conn:
                conn.close()

# Async function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(LogExpense(bot))
