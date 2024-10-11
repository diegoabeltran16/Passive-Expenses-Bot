from discord.ext import commands
from src.utils.db import get_reports_by_user

class GetReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="get_reports", aliases=["obtener_reportes"])
    async def get_reports(self, ctx):
        """
        Command to retrieve reports for the user.
        """
        try:
            # Fetch reports for the user using the user ID
            reports = get_reports_by_user(ctx.author.id)

            # Debug: Print the structure of the reports fetched
            if reports:
                print("Reports fetched from the database:")
                for report in reports:
                    print(report)

            # Check if any reports were found
            if reports and len(reports) > 0:
                # Format the reports using indices after verifying the structure
                report_list = "\n".join([f"ID: {report[0]}, File Path: {report[-1]}" for report in reports])
                await ctx.send(f"Your reports:\n{report_list}")
            else:
                await ctx.send("You have no reports.")
        except Exception as e:
            await ctx.send(f"Failed to retrieve reports: {e}")

async def setup(bot):
    await bot.add_cog(GetReports(bot))
