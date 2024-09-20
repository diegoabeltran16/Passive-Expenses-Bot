# Import necessary modules from discord.ext for creating commands and the database utility for listing expenses.
from discord.ext import commands
from utils.db import list_expenses  # Import the function that retrieves the list of expenses from the database.

# Define a Cog class for handling the "list_expenses" command.
class ListExpenses(commands.Cog):
    """
    A Cog that handles listing all expenses stored in the SQLite database.

    Attributes:
    -----------
    bot : commands.Bot
        The Discord bot instance to which this Cog is added.

    Methods:
    --------
    list_expenses(ctx):
        Retrieves a list of all stored expenses from the database and displays them in the channel.
    """

    def __init__(self, bot):
        """
        Constructor that initializes the bot instance.

        Parameters:
        -----------
        bot : commands.Bot
            The bot instance that will use this Cog.
        """
        self.bot = bot

    @commands.command(name='list_expenses')
    async def list_expenses(self, ctx):
        """
        A command that lists all expenses from the SQLite database and sends them to the Discord channel.

        This command retrieves all logged expenses and formats them into a message that is sent to the
        Discord channel. If no expenses are found, the bot informs the user that there are no logged expenses.

        Parameters:
        -----------
        ctx : commands.Context
            The context in which the command is being invoked, used to interact with the user and the channel.

        Behavior:
        ---------
        - The bot calls the `list_expenses()` function to retrieve all expenses from the database.
        - If no expenses are found, it sends a message indicating "No expenses found."
        - If expenses are found, it formats each expense into a readable message (including the ID, amount, description, and date).
        - The bot sends the formatted list of expenses to the channel.

        Example Usage:
        --------------
        User types the following command in Discord:
        !list_expenses
        
        If expenses are found, the bot responds with:
        "Here are your expenses:
        ID: 1, Amount: 100.0, Description: Lunch at cafe, Date Added: 2024-09-18 12:34:56
        ID: 2, Amount: 50.0, Description: Groceries, Date Added: 2024-09-18 13:40:21"

        If no expenses are found, the bot responds with:
        "No expenses found."
        """
        # Fetch the list of expenses from the database using the db utility function.
        expenses = list_expenses()

        # If no expenses are found, notify the user.
        if not expenses:
            await ctx.send("No expenses found.")
            return

        # Prepare the message that lists all expenses.
        message = "Here are your expenses:\n"
        for expense in expenses:
            message += f"ID: {expense[0]}, Amount: {expense[1]}, Description: {expense[2]}, Date Added: {expense[3]}\n"
        
        # Send the formatted list of expenses to the channel.
        await ctx.send(message)

# Asynchronous setup function to add the Cog to the bot.
async def setup(bot):
    """
    Adds the ListExpenses Cog to the bot.

    Parameters:
    -----------
    bot : commands.Bot
        The bot instance to which this Cog is added.

    Behavior:
    ---------
    - This function is necessary for adding the Cog to the bot asynchronously.
    - It ensures that the Cog is ready and can respond to the 'list_expenses' command.

    Example Usage:
    --------------
    This function is typically called when the bot is initializing to load this command functionality.
    """
    await bot.add_cog(ListExpenses(bot))  # Await the add_cog call to add this Cog to the bot instance.
