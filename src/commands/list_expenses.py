from discord.ext import commands
from utils.db import list_expenses

class ListExpenses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='list_expenses')
    async def list_expenses(self, ctx):
        expenses = list_expenses()
        if not expenses:
            await ctx.send("No expenses found.")
            return
        
        message = "Here are your expenses:\n"
        for expense in expenses:
            message += f"ID: {expense[0]}, Amount: {expense[1]}, Description: {expense[2]}, Date Added: {expense[3]}\n"
        
        await ctx.send(message)

async def setup(bot):  # This needs to be async now
    await bot.add_cog(ListExpenses(bot))
