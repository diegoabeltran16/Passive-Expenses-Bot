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
    async def generate_report(self, ctx, report_format: str = "csv"):
        """
        Command to generate an expense report in the specified format.
        Supported format currently is 'csv'.
        """
        user_id = ctx.author.id
        user_language = 'es'  # Set to user's language

        # Ensure the 'reports' directory exists
        if not os.path.exists('reports'):
            os.makedirs('reports')

        conn = None
        try:
            # Connect to the database
            conn = connect_db()

            # Check if connection was established
            if conn is None:
                raise ValueError("Failed to establish a database connection.")

            # File path for storing the report
            file_path = f"reports/{user_id}_report.{report_format}"

            # Generate the report (CSV by default)
            report = generate_report(conn, user_id, format=report_format, file_path=file_path)

            if report:
                if report_format == 'csv':
                    await ctx.send(translate("csv_report_generated", user_language, file_path=file_path))
                else:
                    await ctx.send(translate("report_generation_failed", user_language, error="Unsupported format"))
            else:
                await ctx.send(translate("report_generation_failed", user_language, error="No data found"))

        except Exception as e:
            # Handle any exceptions that may arise during report generation
            await ctx.send(translate("report_generation_failed", user_language, error=str(e)))

        finally:
            # Close the database connection synchronously
            if conn:
                conn.close()
