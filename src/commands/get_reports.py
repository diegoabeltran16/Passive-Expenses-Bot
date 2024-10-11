import discord
from discord.ext import commands
from src.utils.db import get_reports_by_user

class GetReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='get_reports', aliases=['obtener_reporte'])
    async def get_reports(self, ctx):
        """
        Command to get all reports for a user.
        """
        reports = get_reports_by_user(ctx.author.id)
        if reports:
            report_list = "\n".join([f"ID: {report[0]}, Name: {report[2]}" for report in reports])
            await ctx.send(f"Your reports:\n{report_list}")
        else:
            await ctx.send("No reports found.")

async def setup(bot):
    await bot.add_cog(GetReports(bot))
