from discord.ext import commands
from utils.db import update_expense

class UpdateExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='update_expense')
    async def update_expense(self, ctx, expense_id: int, new_amount: float, new_description: str):
        try:
            update_expense(expense_id, new_amount, new_description)
            await ctx.send(f"Expense with ID {expense_id} updated to {new_amount} for '{new_description}'.")
        except Exception as e:
            await ctx.send(f"Failed to update expense: {str(e)}")

async def setup(bot):  # This needs to be async now
    await bot.add_cog(UpdateExpense(bot))
