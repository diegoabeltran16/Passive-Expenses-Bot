# src/commands/log_expense.py

## General Description 
The main goal of this code is to create a Discord bot command called `log_expense` that allows users to log a new expense into a SQLite database. This command records the user's expenses, provides confirmation messages in the user's preferred language, and ensures the proper handling of database operations.

## Pseudocode

```
1. **Setup and Load Configuration**
   - Set up logging to display informational messages.
   - Load configuration settings from `config.yaml`.

2. **Initialize Database Function**
   - Define a function `initialize_database(db_path)` that checks if the database file exists.
     - If the database file does not exist, create a new SQLite database and initialize the expenses table.

3. **Define LogExpense Cog Class**
   - Define a class `LogExpense` that extends `commands.Cog` to handle the `log_expense` command.
   - In the class constructor, pass the bot instance to the Cog.

4. **Define log_expense Command**
   - Define an asynchronous command `log_expense(ctx, amount: float, *, description: commands.clean_content, conn=None)`.
     - **Parameters:**
       - `ctx`: The context of the command invocation.
       - `amount`: The amount spent.
       - `description`: The description of the expense.
       - `conn`: Optional database connection for testing.
   - Retrieve the user's preferred language from the `user_language` dictionary.
     - Default to English if the user does not have a preference set.
   - Log the user's language preference.
   - Try to perform the following operations:
     1. **Database Connection:**
        - If no connection (`conn`) is provided:
          - Create a directory path for the database.
          - Ensure the directory for the database exists.
          - Initialize the database if necessary.
          - Establish a connection to the SQLite database.
     2. **Insert Expense:**
        - Use `insert_expense()` to add the expense to the database.
        - Retrieve the expense ID of the newly inserted record.
     3. **Generate Response:**
        - Use the `translate()` function to create a response message confirming the expense entry in the user's language.
        - Send the response message to the Discord channel.
   - **Error Handling:**
     - Catch `sqlite3.OperationalError` exceptions, log the error, and inform the user that the database could not be opened.
   - **Cleanup:**
     - Ensure the database connection is closed.

5. **Add the Cog to the Bot**
   - Define an async function `setup(bot)` that adds the `LogExpense` cog to the bot instance.
```

## Code

```
import os
import sqlite3
import logging
from discord.ext import commands
from src.utils.lang import translate
from src.utils.shared import user_language
from src.utils.db import insert_expense, create_expenses_table
import yaml

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load configuration from config.yaml
with open("src/config/config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        create_expenses_table(conn)  # Ensure the table is created
        conn.close()

# Define a Cog class to handle the "log_expense" command
class LogExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='log_expense')
    async def log_expense(self, ctx, amount: float, *, description: commands.clean_content, conn=None):
        """
        Command to log a new expense into the SQLite database.
        
        Parameters:
        ctx: The context of the command invocation.
        amount: The amount spent.
        description: The description of the expense.
        conn: Optional database connection for testing.
        """
        # Retrieve user's preferred language or use default
        user_id = ctx.author.id
        language = user_language.get(ctx.author.id, config.get("default_language", "en"))

        # Log language confirmation
        logging.info(f"User {user_id} is using language: {language}")

        # Use the provided database connection or create a new one if none is provided (for testing)
        try:
            if not conn:
                # Generate an absolute path to the database
                db_directory = os.path.join(os.path.dirname(__file__), "../database")
                db_path = os.path.join(db_directory, "expenses.db")

                # Ensure the directory exists
                if not os.path.exists(db_directory):
                    os.makedirs(db_directory)

                # Initialize the database if needed
                initialize_database(db_path)

                # Create the connection
                conn = sqlite3.connect(db_path)

            # Add the expense to the database
            expense_id = insert_expense(conn, user_id, amount, description)

            # Generate a response in the appropriate language
            response = translate("expense_logged", language, id=expense_id, amount=amount, description=description)

            # Send confirmation message to Discord channel
            await ctx.send(response)
        
        except sqlite3.OperationalError as e:
            logging.error(f"Error: {e}")
            await ctx.send("Could not open the database. Please try again later.")
        finally:
            if conn:
                conn.close()

# Async function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(LogExpense(bot))

```

## Testing 
diegoabeltran16/Passive-Expenses-Bot/tests/test_commands/test_log_expense.py

**Main Goal:**
The main goal of this code is to test the functionality of the `log_expense` command within a Discord bot. The command is supposed to log an expense into an SQLite database, and this test suite verifies both successful expense logging and error handling when there are database issues.

### Testing Pseudocode
```
**1. Imports and Setup**
   - Import necessary modules: `unittest`, `sqlite3`, `discord`, and mocking tools.
   - Add the path to the `src` directory to the system path for correct imports.
   - Import `LogExpense`, `translate`, and `user_language` from `src`.

**2. Define `TestLogExpense` Test Case**
   - **Purpose**: Define the test case for testing the `log_expense` command of the bot.

**3. `asyncSetUp` Method**
   - **Goal**: Set up the testing environment for each test.
   - Define intents and initialize the bot instance.
   - Create an instance of the `LogExpense` cog and add it to the bot.
   - Create a mock context (`ctx`) for testing the command.
   - Patch the database connection method (`connect_db`) to use an in-memory database.
   - Set up an in-memory SQLite database and create an expenses table.

**4. `asyncTearDown` Method**
   - **Goal**: Clean up resources after each test.
   - Close the in-memory database connection.
   - Stop the patched connection.

**5. `test_log_expense_success` Method**
   - **Goal**: Test logging an expense successfully.
   - Mock the user's language preference to "en".
   - Call the `log_expense` command with a test expense (amount: 100.0, description: "Lunch at cafe").
   - Check if the bot sends the correct confirmation message (`"expense_logged"`).

**6. `test_log_expense_error` Method**
   - **Goal**: Test error handling when the database connection fails.
   - Mock the user's language preference to "en".
   - Simulate a database connection failure using `side_effect`.
   - Call the `log_expense` command.
   - Verify that the bot sends the correct error message (`"Could not open the database. Please try again later."`).

**7. `unittest.main()`**
   - Run the test case.

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

from commands.log_expense import LogExpense
from utils.lang import translate
from utils.shared import user_language

class TestLogExpense(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up a test bot and log expense cog before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.log_expense_cog = LogExpense(self.bot)
        await self.bot.add_cog(self.log_expense_cog)
        self.ctx = MagicMock()
        self.ctx.author.id = 1
        self.ctx.send = AsyncMock()

        # Patch the connect_db method in the db module
        self.conn_patcher = patch('utils.db.connect_db')
        self.mock_connect_db = self.conn_patcher.start()

        # Set up an in-memory database for testing
        self.mock_conn = sqlite3.connect(':memory:')
        self.mock_connect_db.return_value = self.mock_conn

        # Import and create the expenses table in the in-memory database
        from utils.db import create_expenses_table
        create_expenses_table(self.mock_conn)

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.mock_conn.close()
        self.conn_patcher.stop()

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_log_expense_success(self, mock_user_language):
        """
        Test logging an expense successfully.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Call the command to log an expense
        await self.log_expense_cog.log_expense(self.ctx, 100.0, description="Lunch at cafe", conn=self.mock_conn)

        # Check if the response was sent correctly
        expected_message = translate("expense_logged", language="en", id=1, amount=100.0, description="Lunch at cafe")
        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_log_expense_error(self, mock_user_language):
        """
        Test logging an expense when the database connection fails.
        """
        mock_user_language[1] = "en"

        # Simulate a database connection failure by setting side_effect
        with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("Unable to connect to the database")):
            # Call the command to log an expense
            await self.log_expense_cog.log_expense(self.ctx, 100.0, description="Lunch at cafe")

            # Check if the error message was sent
            self.ctx.send.assert_called_with("Could not open the database. Please try again later.")

if __name__ == '__main__':
    unittest.main()
``