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

class UpdateExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='update_expense')
    async def update_expense(self, ctx, expense_id: int, new_amount: float, *, new_description: str):
        """
        A command that updates an existing expense in the SQLite database.
        """
        user_id = ctx.author.id
        language = user_language.get(user_id, config.get("default_language", "en"))

        db_directory = os.path.join(os.path.dirname(__file__), "../database")
        db_path = os.path.join(db_directory, "expenses.db")

        if not os.path.exists(db_directory):
            os.makedirs(db_directory)

        initialize_database(db_path)

        try:
            with sqlite3.connect(db_path) as conn:
                db.update_expense(conn, expense_id, new_amount, new_description)

                response = translate("expense_updated", language, id=expense_id, amount=new_amount, description=new_description)
                await ctx.send(response)

        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
            await ctx.send("Could not open the database. Please try again later.")

async def setup(bot):
    await bot.add_cog(UpdateExpense(bot))
