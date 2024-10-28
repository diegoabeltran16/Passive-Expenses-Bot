# src/commands/generate_report.py

import discord
from discord.ext import commands
from src.utils.report_generator import generate_report
from src.utils.file_manager import save_file
from src.utils.lang import translate
from src.utils.shared import get_user_language
from src.utils.db import connect_db

class GenerateReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='generate_report')
    async def generate_report(self, ctx, format: str, start_date: str = None, end_date: str = None, category: str = None):
        """
        Command to generate a report for a user in various formats (text, csv, pdf).
        """
        user_id = ctx.author.id
        user_language = get_user_language(user_id)
        conn = connect_db()  # Establish the database connection

        if not conn:
            await ctx.send(translate("error_connecting_db", user_language))
            return

        try:
            report = generate_report(
                conn=conn,
                user_id=user_id,
                start_date=start_date,
                end_date=end_date,
                category=category,
                format=format
            )

            if format == 'pdf':
                file_path = save_file(report, "reports", f"{user_id}_report.pdf", user_id=user_id)
                await ctx.send(translate("pdf_report_generated", user_language, file_path=file_path))
            elif format == 'text':
                await ctx.send(translate("text_report_generated", user_language) + "\n" + report)
            else:
                raise ValueError(translate("report_format_not_supported", user_language, format=format))
        except Exception as e:
            await ctx.send(translate("report_generation_failed", user_language, error=str(e)))
        finally:
            if conn:
                await conn.close()

async def setup(bot):
    await bot.add_cog(GenerateReport(bot))
