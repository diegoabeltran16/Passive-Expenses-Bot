# src/commands/generate_report.py

import os
import logging
from discord.ext import commands
from src.utils.report_generator import generate_report
from src.utils.file_manager import save_file
from src.utils.lang import translate
from src.utils.shared import get_user_language
from src.utils.db import connect_db

# Ensure logging is configured
logging.basicConfig(level=logging.INFO)

class GenerateReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='generate_report', aliases=['generar_reporte'])
    async def generate_report(self, ctx, start_date: str = None, end_date: str = None, category: str = None, report_format: str = "csv"):
        """
        Command to generate a report for a user in various formats (text, csv).
        
        Parameters:
        - start_date, end_date, category: Filters for the report.
        - report_format: Format of the report. Options are 'text', 'csv'.
        """
        user_id = ctx.author.id
        user_language = get_user_language(user_id)

        logging.info(f"Generating report for user {user_id} with format {report_format}")
        
        # Validate the report format
        if report_format.lower() not in ["text", "csv"]:
            await ctx.send(translate("report_format_not_supported", user_language, format=report_format))
            return

        # Establish a database connection
        conn = connect_db()
        if not conn:
            await ctx.send(translate("error_connecting_db", user_language))
            return

        try:
            # Create the directory for saving reports if needed
            reports_dir = os.path.join("reports")
            os.makedirs(reports_dir, exist_ok=True)
            
            # Prepare the file path for CSV if the format is CSV
            file_path = os.path.join(reports_dir, f"{user_id}_report.csv") if report_format == "csv" else None

            # Generate the report with provided filters
            report = generate_report(
                conn=conn,
                user_id=user_id,
                start_date=start_date,
                end_date=end_date,
                category=category,
                format=report_format,
                file_path=file_path
            )

            # Check if report is empty or None
            if not report:
                logging.info("No data found for the specified parameters.")
                await ctx.send(translate("report_generation_failed", user_language, error="No data found for the specified parameters."))
                return

            # Send report based on format
            if report_format.lower() == 'csv':
                await ctx.send(translate("csv_report_generated", user_language, file_path=file_path))
            elif report_format.lower() == 'text':
                await ctx.send(translate("text_report_generated", user_language) + "\n" + report)

        except Exception as e:
            # Log and send error message if report generation fails
            logging.error(f"Error generating report: {e}")
            await ctx.send(translate("report_generation_failed", user_language, error=str(e)))

        finally:
            # Close the database connection
            if conn:
                conn.close()

# Async function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(GenerateReport(bot))
