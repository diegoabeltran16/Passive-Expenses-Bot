from discord.ext import commands
from utils import db  # Import the db module where your database functions are located

class LogExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, description: str):
        # Add the expense to the SQLite database
        expense_id = db.add_expense(amount, description)

        # Confirm the expense has been logged by sending a message to the Discord channel
        await ctx.send(f'Expense logged with ID {expense_id}: {amount} for {description}')

async def setup(bot):  # This needs to be async now
    await bot.add_cog(LogExpense(bot))  # Await the add_cog call
