import os
import sqlite3
import logging
from discord.ext import commands
from src.utils.lang import translate
from src.utils import db  # Import the db module for database functions
from src.utils.shared import get_user_language  # Replace user_language dictionary with function
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
        db.create_expenses_table(conn)  # Ensure the expenses table is created
        conn.close()

class UpdateExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='update_expense', aliases=['actualizar_gasto'])
    async def update_expense(self, ctx, expense_id: int, new_amount: float, *, new_description: str):
        """
        A command that updates an existing expense in the SQLite database.
        
        Parameters:
        ctx: The context of the command invocation.
        expense_id: The ID of the expense to update.
        new_amount: The updated amount of the expense.
        new_description: The updated description of the expense.
        """
        user_id = ctx.author.id

        # Fetch the user's preferred language from the database
        language = get_user_language(user_id)

        # Generate an absolute path to the database
        db_directory = os.path.join(os.path.dirname(__file__), "../database")
        db_path = os.path.join(db_directory, "expenses.db")

        # Ensure the directory exists
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)

        # Initialize the database if needed
        initialize_database(db_path)

        try:
            with sqlite3.connect(db_path) as conn:
                # Call the update function from db module
                db.update_expense(conn, expense_id, new_amount, new_description)

                # Use the translate function to generate a response in the user's language
                response = translate("expense_updated", language, id=expense_id, amount=new_amount, description=new_description)

                # Send the translated response to the Discord channel
                await ctx.send(response)

        except sqlite3.OperationalError as e:
            logging.error(f"Error opening database: {e}")
            await ctx.send(translate("error_connecting_db", language, error=str(e)))

async def setup(bot):
    await bot.add_cog(UpdateExpense(bot))
