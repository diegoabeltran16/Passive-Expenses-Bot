# src/commands/delete_expense.py

## General Description
The core functionality of this code is to ensure that users can seamlessly interact with their expense data on Discord, providing easy deletion of records while handling language preferences and ensuring robust error handling.

## Pseudo Code

```
1. **Import necessary modules**
   - Import commands from Discord library.
   - Import translation module, database functions, user language preferences, and configuration management.

2. **Load configuration from file**
   - Define the path to the configuration file (`config.yaml`).
   - Open and load configuration settings from the file.

3. **Define function to initialize database if not exists**
   - If the database file does not exist:
     - Create a connection to the database.
     - Call function to create the `expenses` table.
     - Close the database connection.

4. **Define a class for DeleteExpense Command (a Cog)**
   - Define a class named `DeleteExpense`:
     - **Constructor**:
       - Takes `bot` as input and stores it.
     
     - **Define command `delete_expense`**:
       - **Parameters**: The context (`ctx`) and `expense_id` (integer).
       - **Description**: Deletes a specific expense from the database.

       1. **Retrieve user language**:
          - Get the user's language preference using `user_id`.
          - If no preference exists, use the default language from the configuration.

       2. **Generate database path**:
          - Define the directory for the database.
          - Define the full path for the `expenses.db` file.
          - If the directory does not exist, create it.
          - Call function to initialize the database if necessary.

       3. **Connect to the database and delete expense**:
          - Use a `try` block to connect to the database.
          - Call function to delete expense from the database using `expense_id`.
          - Generate a response using the `translate` function based on the user's language.
          - Send the response message to the Discord channel.

       4. **Handle database connection errors**:
          - If there is an error connecting to the database:
            - Print the error message.
            - Send an error response to the Discord channel.

5. **Define an asynchronous function to add the Cog to the bot**
   - Define function `setup` that takes `bot` as input.
   - Add the `DeleteExpense` Cog to the bot.

## Summary of Key Steps:
- **Load Configuration**: Read settings from a YAML configuration file.
- **Initialize Database**: Create a database and ensure that the required table exists.
- **Define Cog with Command**:
  - Create a command (`delete_expense`) to delete an expense from the database.
  - Use the user’s preferred language for responses.
- **Handle Database Operations**: Ensure proper database management (connection, creation, deletion).
- **Add Cog to Bot**: Make the `delete_expense` command available in the bot.

```

## Code

```
import os
import sqlite3
from discord.ext import commands
from src.utils.lang import translate  # Import the translation module for multilingual responses
from src.utils import db  # Import the db module where database functions are located.
from src.utils.shared import user_language  # Import user_language dictionary to access user language preferences
import yaml

# Load configuration from config.yaml
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Function to initialize the database if it doesn't exist
def initialize_database(db_path):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        db.create_expenses_table(conn)  # Ensure the table is created
        conn.close()

# Define a Cog class to handle the "delete_expense" command.
class DeleteExpense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_expense')
    async def delete_expense(self, ctx, expense_id: int):
        """
        A command that deletes an expense from the SQLite database.
        """
        # Get the user's preferred language, defaulting to 'en' if not set
        user_id = ctx.author.id
        language = user_language.get(user_id, config.get("default_language", "en"))

        # Generate an absolute path to the database
        db_directory = os.path.join(os.path.dirname(__file__), "../database")
        db_path = os.path.join(db_directory, "expenses.db")

        # Ensure the directory exists
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)

        # Initialize the database if needed
        initialize_database(db_path)

        # Connect to the database and delete the expense
        try:
            with sqlite3.connect(db_path) as conn:
                db.delete_expense(conn, expense_id)

                # Use the translation function to generate a response in the user's language
                response = translate("expense_deleted", language, id=expense_id)

                # Send the translated response to the Discord channel
                await ctx.send(response)

        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
            await ctx.send("Could not open the database. Please try again later.")

# Asynchronous function to add the Cog to the bot.
async def setup(bot):
    await bot.add_cog(DeleteExpense(bot))

```

## Testing 
diegoabeltran16/Passive-Expenses-Bot/tests/test_commands/test_delete_expense.py

**Main Goal:**
The main goal of the `TestDeleteExpense` test class is to verify that the `delete_expense` command in the Discord bot correctly deletes an expense from the SQLite database and sends the appropriate response message to the user. It also tests how the command handles cases when the database connection fails.

### Testing Pseudocode
```
1. **Import necessary modules:**
   - Import `unittest` for testing.
   - Import `sqlite3`, `discord`, and `os` for database and Discord bot integration.
   - Import `MagicMock`, `AsyncMock`, and `patch` for mocking functions and methods.
   - Import necessary bot classes from `discord.ext.commands`.
   - Add the correct path to access the source directory.
   - Import the `DeleteExpense` command cog, translation function, and shared user language dictionary.

2. **Define the `TestDeleteExpense` class that inherits from `unittest.IsolatedAsyncioTestCase`.**

3. **Define `asyncSetUp` method to prepare the test environment:**
   - Set up a test bot instance with command prefix and intents.
   - Add the `DeleteExpense` cog to the bot.
   - Create a mock context object with attributes `author.id` and `send`.
   - Patch the `connect_db` method to return an in-memory database for testing purposes.
   - Create the expenses table in the in-memory database.
   - Insert an expense into the database for deletion in the test.

4. **Define `asyncTearDown` method to clean up after each test:**
   - Close the in-memory database connection.
   - Stop the patched connection method.

5. **Define `test_delete_expense_success` method to test successful deletion of an expense:**
   - Patch the `user_language` dictionary to set the user's language preference to English.
   - Call the `delete_expense` command with the test context and the expense ID.
   - Assert that the correct success response was sent to the user by verifying the translated message.

6. **Define `test_delete_expense_error` method to test deleting an expense when the database connection fails:**
   - Patch the `user_language` dictionary to set the user's language preference to English.
   - Simulate a database connection failure by patching `sqlite3.connect` to raise an `OperationalError`.
   - Call the `delete_expense` command with the test context and the expense ID.
   - Assert that the appropriate error message was sent to the user.

7. **Run the test cases if the file is executed as the main program.**


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

from commands.delete_expense import DeleteExpense
from utils.lang import translate
from utils.shared import user_language

class TestDeleteExpense(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Set up a test bot and delete expense cog before each test.
        """
        intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.delete_expense_cog = DeleteExpense(self.bot)
        await self.bot.add_cog(self.delete_expense_cog)
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
        from utils.db import create_expenses_table, insert_expense
        create_expenses_table(self.mock_conn)

        # Insert an expense to delete in the test
        self.expense_id = insert_expense(self.mock_conn, user_id=1, amount=100.0, description="Test expense")

    async def asyncTearDown(self):
        """
        Clean up after each test.
        """
        self.mock_conn.close()
        self.conn_patcher.stop()

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_delete_expense_success(self, mock_user_language):
        """
        Test deleting an expense successfully.
        """
        # Set the user's language preference
        mock_user_language[1] = "en"

        # Call the command to delete an expense
        await self.delete_expense_cog.delete_expense(self.ctx, self.expense_id)

        # Check if the response was sent correctly
        expected_message = translate("expense_deleted", language="en", id=self.expense_id)
        self.ctx.send.assert_called_with(expected_message)

    @patch('utils.shared.user_language', new_callable=dict)
    async def test_delete_expense_error(self, mock_user_language):
        """
        Test deleting an expense when the database connection fails.
        """
        mock_user_language[1] = "en"

        # Simulate a database connection failure by setting side_effect
        with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("Unable to connect to the database")):
            # Call the command to delete an expense
            await self.delete_expense_cog.delete_expense(self.ctx, self.expense_id)

            # Check if the error message was sent
            self.ctx.send.assert_called_with("Could not open the database. Please try again later.")

if __name__ == '__main__':
    unittest.main()
```