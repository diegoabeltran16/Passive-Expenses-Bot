import os
import logging
from discord.ext import commands
from src.utils.report_generator import generate_report  # Report generation logic
from src.utils.file_manager import save_file  # File saving utility
from src.utils.lang import translate  # Language/translation utility
from src.utils.shared import get_user_language  # User language preference utility
from src.utils.db import connect_db  # Database connection utility

# Ensure logging is configured
logging.basicConfig(level=logging.INFO)

class GenerateReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='generate_report', aliases=['generar_reporte'])
    async def generate_report(self, ctx, report_format: str = "csv", start_date: str = None, end_date: str = None, category: str = None):
        """
        Command to generate a report for a user in various formats (text, csv, pdf).
        
        Parameters:
        - report_format: Format of the report. Options are 'text', 'csv', 'pdf'.
        - start_date, end_date, category: Filters for the report.
        """
        user_id = ctx.author.id
        user_language = get_user_language(user_id)

        logging.info(f"Generating report for user {user_id} with format {report_format}")
        
        # Establish database connection
        conn = connect_db()
        if not conn:
            await ctx.send(translate("error_connecting_db", user_language))
            return

        try:
            # Generate the report data
            report = generate_report(
                conn=conn,
                user_id=user_id,
                start_date=start_date,
                end_date=end_date,
                category=category,
                format=report_format
            )

            # Handle output based on specified format
            if report_format.lower() == 'pdf':
                # Ensure the 'reports' directory exists
                reports_dir = os.path.join("reports")
                os.makedirs(reports_dir, exist_ok=True)

                file_path = save_file(report, reports_dir, f"{user_id}_report.pdf", user_id=user_id)
                await ctx.send(translate("pdf_report_generated", user_language, file_path=file_path))

            elif report_format.lower() == 'text':
                await ctx.send(translate("text_report_generated", user_language) + "\n" + report)

            elif report_format.lower() == 'csv':
                # Save as a CSV file
                reports_dir = os.path.join("reports")
                os.makedirs(reports_dir, exist_ok=True)

                file_path = save_file(report, reports_dir, f"{user_id}_report.csv", user_id=user_id)
                await ctx.send(translate("csv_report_generated", user_language, file_path=file_path))

            else:
                # Unsupported format
                await ctx.send(translate("report_format_not_supported", user_language, format=report_format))

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
