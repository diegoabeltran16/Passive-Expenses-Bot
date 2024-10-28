import sqlite3
from discord.ext import commands
from src.utils.lang import translate
from src.utils.report_generator import generate_report
from src.utils.db import connect_db
import os

class GenerateReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='generate_report', aliases=['generar_reporte'])
    async def generate_report(self, ctx, report_format: str = "pdf"):
        """
        Command to generate an expense report in the specified format.
        Supported formats are 'pdf' and 'csv'.
        """
        user_id = ctx.author.id
        user_language = 'es'  # Fetch user's language preference if applicable.

        # Ensure the 'reports' directory exists
        reports_directory = "reports"
        self.ensure_directory_exists(reports_directory)

        try:
            # Connect to the database
            with connect_db() as conn:
                if conn is None:
                    raise ValueError("Failed to establish a database connection.")

                # Choose the file path for storing the report
                file_path = os.path.join(reports_directory, f"{user_id}_report.{report_format}")

                # Generate the report based on the chosen format
                report_file_path = generate_report(conn, user_id, format=report_format, file_path=file_path)

                if report_file_path:
                    if report_format == 'pdf':
                        await ctx.send(translate("pdf_report_generated", user_language, file_path=report_file_path))
                    elif report_format == 'csv':
                        await ctx.send(translate("csv_report_generated", user_language, file_path=report_file_path))
                else:
                    await ctx.send(translate("report_generation_failed", user_language, error="No data found"))

        except sqlite3.Error as db_err:
            await ctx.send(translate("error_connecting_db", user_language, error=str(db_err)))
        except Exception as e:
            # Send an error message if anything goes wrong
            await ctx.send(translate("report_generation_failed", user_language, error=str(e)))

    def ensure_directory_exists(self, directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

# Asynchronous function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(GenerateReport(bot))
