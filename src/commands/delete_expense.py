from discord.ext import commands

class DeleteExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_expense')
    async def delete_expense(self, ctx, expense_id: int):
        # Placeholder logic for now
        await ctx.send(f'Expense with ID {expense_id} deleted.')

def setup(bot):
    bot.add_cog(DeleteExpense(bot))
