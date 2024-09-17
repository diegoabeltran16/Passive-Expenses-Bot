from discord.ext import commands

class LogExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, description: str):
        print(f'log_expense command triggered with amount: {amount}, description: {description}')
        await ctx.send(f'Expense logged: {amount} for {description}')

async def setup(bot):  # This needs to be async now
    await bot.add_cog(LogExpense(bot))  # Await the add_cog call
