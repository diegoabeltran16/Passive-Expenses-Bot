from discord.ext import commands
from utils import db  # Import the db module where your database functions are located

class DeleteExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_expense')
    async def delete_expense(self, ctx, expense_id: int):
        # Call the delete_expense function from the database
        db.delete_expense(expense_id)

        # Confirm the expense has been deleted by sending a message to the Discord channel
        await ctx.send(f'Expense with ID {expense_id} deleted.')

async def setup(bot):  # This needs to be async now
    await bot.add_cog(DeleteExpense(bot))  # Await the add_cog call
