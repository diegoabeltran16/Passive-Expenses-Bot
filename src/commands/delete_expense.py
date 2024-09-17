from discord.ext import commands

class DeleteExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_expense')
    async def delete_expense(self, ctx, expense_id: int):
        print(f'delete_expense command triggered with ID: {expense_id}')
        await ctx.send(f'Expense with ID {expense_id} deleted.')

async def setup(bot):  # This needs to be async now
    await bot.add_cog(DeleteExpense(bot))  # Await the add_cog call
