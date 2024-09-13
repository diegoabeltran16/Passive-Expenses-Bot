from discord.ext import commands

class LogExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, description: str):
        # Placeholder logic for now
        await ctx.send(f'Expense logged: {amount} for {description}')

def setup(bot):
    bot.add_cog(LogExpense(bot))
