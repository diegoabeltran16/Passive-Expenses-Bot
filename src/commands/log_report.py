import discord
from discord.ext import commands
from src.utils.db import insert_report

class LogReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_report', aliases=['ingresar_reporte'])
    async def log_report(self, ctx, report_name: str, file_path: str):
        """
        Command to log a report for a user.
        """
        try:
            # Call insert_report with all the necessary arguments
            report_id = insert_report(ctx.author.id, report_name, file_path)
            if report_id:
                await ctx.send(f"Report logged successfully with ID {report_id}.")
            else:
                await ctx.send("Error logging report.")
        except Exception as e:
            await ctx.send(f"An error occurred while logging the report: {e}")

async def setup(bot):
    await bot.add_cog(LogReport(bot))
