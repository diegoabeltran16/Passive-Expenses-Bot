import discord
from discord.ext import commands
from src.utils.db import insert_report

class LogReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_report', aliases=['ingresar_reporte'])
    async def log_report(self, ctx, report_name, file_path):
        """
        Command to log a report for a user.
        """
        report_id = insert_report(ctx.author.id, report_name, file_path)
        if report_id:
            await ctx.send(f"Report logged successfully with ID {report_id}.")
        else:
            await ctx.send("Error logging report.")

async def setup(bot):
    await bot.add_cog(LogReport(bot))
