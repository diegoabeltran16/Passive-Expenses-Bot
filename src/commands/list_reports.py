# src/commands/list_reports.py

import discord
from discord.ext import commands
from src.utils.db import get_reports_by_user
from src.utils.lang import translate
from src.utils.shared import get_user_language

class ListReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='list_reports', aliases=['listar_reportes'])
    async def list_reports(self, ctx):
        """
        Command to list all reports for a user.
        """
        user_id = ctx.author.id
        user_language = get_user_language(user_id)

        try:
            reports = get_reports_by_user(user_id)
            if reports:
                report_list = "\n".join(
                    [f"ID: {r['report_id']}, File Path: {r['file_path']}" for r in reports]
                )
                message = translate('reports_listed', user_language, reports=report_list)
            else:
                message = translate('no_reports_found', user_language)

            await ctx.send(message)
        except Exception as e:
            await ctx.send(translate('error_retrieving_reports', user_language, error=str(e)))

async def setup(bot):
    await bot.add_cog(ListReports(bot))
