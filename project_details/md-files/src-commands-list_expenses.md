# src/commands/list_expenses.py

## Descripción General
The primary goal of this code is to provide a command within a Discord bot that allows users to log expenses into an SQLite database. The bot is intended to interact with users through a chat command called log_expense, which takes an amount and description, saves the details to a local SQLite database, and returns a confirmation message in the user's preferred language. The solution ensures proper database setup, error handling, and multi-language support to provide a smooth user experience.

## Pseudo Codigo

```
1. **Setup**:
   - Import necessary libraries (e.g., `os`, `sqlite3`, `logging`, `discord.ext.commands`, etc.).
   - Set up logging for debugging purposes.
   - Load configuration settings from `config.yaml`.

2. **Function to Initialize Database**:
   - Define `initialize_database(db_path)`:
     - If the database file does not exist:
       - Create a connection to the SQLite database.
       - Call `create_expenses_table(conn)` to create necessary tables.
       - Close the connection.

3. **Define a Cog Class to Log Expenses**:
   - Define class `LogExpense(commands.Cog)`:
     - **Constructor** (`__init__`):
       - Assign bot instance to the class.
     - **Command Definition** (`log_expense`):
       - Define an asynchronous command `log_expense(ctx, amount, description, conn=None)`:
         - Retrieve the user ID and preferred language from `user_language` or use the default (`en`).
         - Log the user language confirmation.
         - If no connection is provided, create a new database connection:
           - Determine the path for the database.
           - If the directory does not exist, create it.
           - Call `initialize_database(db_path)` to set up the database.
           - Create a new database connection.
         - Insert the expense into the database using `insert_expense()`.
         - Translate the response message into the appropriate language.
         - Send the confirmation message to the user via the Discord channel.
       - **Error Handling**: Catch any database connection errors and notify the user.
       - **Cleanup**: Ensure the database connection is closed after use.

4. **Add the Cog to the Bot**:
   - Define an asynchronous function `setup(bot)` that adds the `LogExpense` cog to the bot.


```

## Code

```
import os
import sqlite3
from discord.ext import commands
from src.utils.lang import translate
from src.utils import db
from src.utils.shared import user_language
import yaml

# Load configuration from config.yaml
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        db.create_expenses_table(conn)
        conn.close()

class ListExpenses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='list_expenses')
    async def list_expenses(self, ctx, conn=None):
        """
        A command that lists all expenses from the SQLite database and sends them to the Discord channel.
        Parameters:
        ctx: The context of the command invocation.
        conn: Optional database connection for testing.
        """
        user_id = ctx.author.id
        language = user_language.get(user_id, config.get("default_language", "en"))

        if not conn:
            # Generate an absolute path to the database
            db_directory = os.path.join(os.path.dirname(__file__), "../database")
            db_path = os.path.join(db_directory, "expenses.db")

            # Ensure the directory exists
            if not os.path.exists(db_directory):
                os.makedirs(db_directory)

            # Initialize the database if needed
            initialize_database(db_path)

            try:
                conn = sqlite3.connect(db_path)
            except sqlite3.OperationalError as e:
                print(f"Error: {e}")
                await ctx.send("Could not open the database. Please try again later.")
                return

        try:
            expenses = db.list_expenses(conn, user_id)

            if not expenses:
                response = translate("no_expenses_found", language)
            else:
                response = translate("here_are_your_expenses", language) + "\n"
                for expense in expenses:
                    response += f"ID: {expense[0]}, Amount: {expense[2]}, Description: {expense[3]}, Date Added: {expense[5]}\n"

            await ctx.send(response)

        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
            await ctx.send("Could not open the database. Please try again later.")

# Async function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(ListExpenses(bot))

```

## Testing 
diegoabeltran16/Passive-Expenses-Bot/tests/test_commands/test_list_expenses.py

**Main Goal:**

The main goal of this code is to test the list_expenses command of a Discord bot, which is used to list a user's expenses stored in an SQLite database. The tests cover multiple scenarios including when there are no expenses, when expenses are present, and when there is an error connecting to the database. The tests ensure that the bot sends the appropriate response to the user in each scenario.

### Testing Pseudocode
```
1. **Import necessary modules**
   - Import standard modules such as `os`, `sqlite3`, and `unittest`.
   - Import Discord-related modules for bot interaction.
   - Import the `ListExpenses` cog and helper functions.

2. **Set up test class for `list_expenses` command**
   - Create a test class that inherits from `unittest.IsolatedAsyncioTestCase` to test asynchronous code.

3. **Define `asyncSetUp` method**
   - Create a bot instance with command prefix `!` and default intents.
   - Add the `ListExpenses` cog to the bot.
   - Set up a mock context (`ctx`) with `send` method to simulate Discord responses.
   - Set up an in-memory SQLite database connection for testing purposes.
   - Create an `expenses` table in the in-memory database.

4. **Define `asyncTearDown` method**
   - Close the database connection after each test.

5. **Define test for listing expenses when there are no expenses**
   - Patch `user_language` to mock the user's preferred language.
   - Set the user's language to English (`en`).
   - Ensure the database has no expenses by deleting all entries.
   - Call the `list_expenses` command with the mock context and database connection.
   - Verify that the bot sends the appropriate message: "No expenses found."

6. **Define test for listing expenses when expenses are present**
   - Patch `user_language` to mock the user's preferred language.
   - Set the user's language to English (`en`).
   - Insert a mock expense into the in-memory database.
   - Fetch the inserted expense details to dynamically construct the expected message.
   - Call the `list_expenses` command with the mock context and database connection.
   - Verify that the bot sends the appropriate message including the expense details.

7. **Define test for listing expenses when the database connection fails**
   - Patch `user_language` to mock the user's preferred language.
   - Simulate a database connection failure using `patch` on `sqlite3.connect`.
   - Call the `list_expenses` command with the mock context.
   - Verify that the bot sends an error message: "Could not open the database. Please try again later."

8. **Run the tests**
   - Execute the tests using `unittest.main()`.


```

### Testing Code
```
import unittest
import sys
import os
import sqlite3
import discord
from unittest.mock import MagicMock, AsyncMock, patch
from discord.ext import commands

# Add the correct path for imports to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from commands.list_expenses import ListExpenses
from utils.lang import translate
from utils.shared import user_language
from utils.db import create_expenses_table

class TestListExpenses(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up a test bot and list expenses cog before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.list_expenses_cog = ListExpenses(self.bot)
        await self.bot.add_cog(self.list_expenses_cog)
        self.ctx = MagicMock()
        self.ctx.author.id = 1
        self.ctx.send = AsyncMock()

        # Set up an in-memory database for testing
        self.mock_conn = sqlite3.connect(':memory:')
        
        # Create the expenses table in the in-memory database
        create_expenses_table(self.mock_conn)

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.mock_conn.close()

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_list_expenses_no_expenses(self, mock_user_language):
        """
        Test listing expenses when no expenses are found.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Ensure the database has no expenses
        cursor = self.mock_conn.cursor()
        cursor.execute("DELETE FROM expenses")
        self.mock_conn.commit()

        # Call the command to list expenses when there are no expenses
        await self.list_expenses_cog.list_expenses(self.ctx, conn=self.mock_conn)

        # Check if the response was sent correctly
        expected_message = translate("no_expenses_found", language="en")
        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_list_expenses_with_expenses(self, mock_user_language):
        """
        Test listing expenses when expenses are present.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Insert a mock expense into the database
        cursor = self.mock_conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (user_id, amount, description, category, date_added)
            VALUES (?, ?, ?, ?, datetime('now'))
        ''', (1, 50.0, "Grocery shopping", "Groceries"))
        self.mock_conn.commit()

        # Fetch the date_added for the expense to construct the expected message dynamically
        cursor.execute("SELECT id, amount, description, date_added FROM expenses WHERE user_id = ?", (1,))
        expense = cursor.fetchone()
        expense_id, amount, description, date_added = expense

        # Call the command to list expenses
        await self.list_expenses_cog.list_expenses(self.ctx, conn=self.mock_conn)

        # Construct the expected message dynamically
        expected_message = translate("here_are_your_expenses", language="en") + "\n"
        expected_message += f"ID: {expense_id}, Amount: {amount}, Description: {description}, Date Added: {date_added}\n"

        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_list_expenses_db_error(self, mock_user_language):
        """
        Test listing expenses when the database connection fails.
        """
        mock_user_language[1] = "en"

        # Simulate a database connection failure by setting side_effect
        with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("Unable to connect to the database")):
            # Call the command to list expenses
            await self.list_expenses_cog.list_expenses(self.ctx)

            # Check if the error message was sent
            self.ctx.send.assert_called_with("Could not open the database. Please try again later.")

if __name__ == '__main__':
    unittest.main()
```