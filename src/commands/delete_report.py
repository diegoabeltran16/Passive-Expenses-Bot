import discord
from discord.ext import commands
from src.utils.db import delete_report as db_delete_report
from src.utils.file_manager import delete_file
from src.utils.lang import translate

class DeleteReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_report', aliases=['eliminar_reporte'])
    async def delete_report(self, ctx, report_id: int):
        """
        Command to delete a report by its ID.
        """
        user_language = 'en'  # This should be dynamically retrieved based on user settings
        try:
            # Call the delete_report function with the report ID
            file_path = db_delete_report(report_id)

            if file_path is None:
                await ctx.send(translate('no_report_found', user_language, id=report_id))
                return

            # Attempt to delete the file if it exists
            if delete_file(file_path):
                await ctx.send(translate("report_deleted_confirmation", user_language, id=report_id))
            else:
                await ctx.send(translate("error_deleting_report", user_language, error="File not found"))

        except Exception as e:
            await ctx.send(translate("error_deleting_report", user_language, error=str(e)))

async def setup(bot):
    await bot.add_cog(DeleteReport(bot))
