import discord
from discord.ext import commands
from src.utils.db import delete_report

class DeleteReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_report', aliases=['eliminar_reporte'])
    async def delete_report(self, ctx, report_id: int):
        """
        Command to delete a report by its ID.
        """
        delete_report(report_id)
        await ctx.send(f"Report with ID {report_id} deleted.")

async def setup(bot):
    await bot.add_cog(DeleteReport(bot))
