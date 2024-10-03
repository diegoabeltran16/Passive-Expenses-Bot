# src/utils/db.py

## General description
This Python file defines the core database operations for managing expenses and budgets in a SQLite database. It provides helper functions to create, retrieve, update, and delete entries from the expenses and budgets tables. The database operations are used by the Passive Expenses Bot to track user expenses, categorize them, and check against predefined budgets.

## Pseudocode for Each Section 

1. Database Connection Helper
```
Function: connect_db()

Establish a connection to the SQLite database (expenses.db).
Return the connection object for further use.
```

2. Table Creation

```
Function: create_expenses_table()

Connect to the database.
Create the expenses table with the following columns:
id: Primary key.
user_id: ID of the user who logged the expense.
amount: The amount spent.
description: Description of the expense.
category: Category of the expense (optional).
date_added: Timestamp for when the expense was logged.
Close the database connection.
Function: create_budgets_table()

Connect to the database.
Create the budgets table with the following columns:
id: Primary key.
user_id: ID of the user setting the budget.
category: Category the budget applies to.
limit: Spending limit (escaped as "limit" due to being an SQL keyword).
period: Budget period (e.g., monthly).
start_date: The start of the budget period.
end_date: The end of the budget period.
Close the database connection.
```

3. Drop Tables
```
Function: drop_tables()

Drop the expenses and budgets tables if they exist.
Useful for resetting the database schema.
```
4. Insert Data
```
Function: insert_expense()

Insert a new expense into the expenses table.
Requires user_id, amount, description, and optionally a category.
Commit the transaction and close the connection.
Function: insert_budget()

Insert a new budget into the budgets table.
Requires user_id, category, limit, period, start_date, and end_date.
Commit the transaction and close the connection.
```
5. Retrieve Data
```
Function: get_budget_by_category()

Retrieve a budget for a specific user_id and category.
Return the result if found; otherwise, return None.
Function: get_expenses_by_category()

Retrieve all expenses for a specific user_id and category.
Optionally, filter by start_date and end_date.
Return the result as a list of expenses.

```
6. Update Data
```
Function: update_budget()

Update the limit of an existing budget by budget_id.
Commit the transaction and close the connection.
Function: update_expense_category()

Update the category of an existing expense by expense_id.
Commit the transaction and close the connection.
```
7. Delete Data
```
Function: delete_budget()

Delete a budget by its budget_id.
Commit the transaction and close the connection.
```
8. Calculations
```
Function: get_total_expenses()

Calculate the total expenses for a specific user_id, category, and period (start_date to end_date).
Return the total amount spent in the period.
```
9. Budget Tracking
```
Function: check_budget_status()

Calculate total expenses for a user_id and category in a given period.
Retrieve the budget for that category.
Compare the total expenses with the budget limit.
Return a message indicating whether the user has exceeded their budget or is within it.
```
10. Expense Reporting
```
Function: generate_expense_report()

Retrieve and group expenses by category for a specific time period.
Format the data as a readable expense report (text-based).
Return the formatted report.
```
11. Initializa the Tables
```
At the end of the file:

Call create_expenses_table() and create_budgets_table() to ensure the tables are created when the bot starts.
```

## Code

```
import sqlite3

# Database connection helper function
def connect_db():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect('expenses.db')

# Create the expenses table if it doesn't exist
def create_expenses_table():
    """Creates the 'expenses' table in the database if it doesn't already exist."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,  -- Add user_id column here
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Create the budgets table
def create_budgets_table():
    """Creates the 'budgets' table in the database if it doesn't already exist."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            "limit" REAL NOT NULL,  -- Escape 'limit' keyword here
            period TEXT NOT NULL,
            start_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Drop tables
def drop_tables():
    """Drops the expenses and budgets tables if they exist."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS expenses')
    cursor.execute('DROP TABLE IF EXISTS budgets')

    conn.commit()
    conn.close()

# Insert a new expense
def insert_expense(user_id, amount, description, category=None):
    """Inserts a new expense into the 'expenses' table."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO expenses (user_id, amount, description, category)
        VALUES (?, ?, ?, ?)
    ''', (user_id, amount, description, category))

    conn.commit()
    conn.close()

# Insert a new budget
def insert_budget(user_id, category, limit, period, start_date, end_date):
    """Inserts a new budget into the 'budgets' table."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO budgets (user_id, category, "limit", period, start_date, end_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, category, limit, period, start_date, end_date))

    conn.commit()
    conn.close()

# Retrieve a budget by category for a user
def get_budget_by_category(user_id, category):
    """Retrieves the budget for a specific category and user."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM budgets WHERE user_id = ? AND category = ?
    ''', (user_id, category))

    budget = cursor.fetchone()
    conn.close()

    return budget

# Update an existing budget
def update_budget(budget_id, new_limit):
    """Updates the limit of an existing budget."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE budgets
        SET "limit" = ?  -- Escape the 'limit' keyword here
        WHERE id = ?
    ''', (new_limit, budget_id))

    conn.commit()
    conn.close()


# Delete a budget by its ID
def delete_budget(budget_id):
    """Deletes a budget by its ID."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM budgets WHERE id = ?', (budget_id,))
    conn.commit()
    conn.close()

# Update the category of an existing expense
def update_expense_category(expense_id, category):
    """Updates the category of an existing expense."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE expenses
        SET category = ?
        WHERE id = ?
    ''', (category, expense_id))

    conn.commit()
    conn.close()

# Retrieve expenses by category
def get_expenses_by_category(user_id, category, start_date=None, end_date=None):
    """Retrieves all expenses by category for a specific user."""
    conn = connect_db()
    cursor = conn.cursor()

    query = 'SELECT * FROM expenses WHERE category = ? AND user_id = ?'
    params = [category, user_id]

    # Filter by date range if provided
    if start_date and end_date:
        query += ' AND date_added BETWEEN ? AND ?'
        params.extend([start_date, end_date])

    cursor.execute(query, params)
    expenses = cursor.fetchall()
    conn.close()

    return expenses

# Calculate total expenses for a category in a given period
def get_total_expenses(user_id, category, start_date, end_date):
    """Calculates the total expenses for a given category and period."""
    conn = connect_db()
    cursor = conn.cursor()

    query = '''
        SELECT SUM(amount) FROM expenses
        WHERE user_id = ? AND category = ? AND date_added BETWEEN ? AND ?
    '''
    cursor.execute(query, (user_id, category, start_date, end_date))

    total = cursor.fetchone()[0]
    conn.close()

    # If there are no expenses, return 0 instead of None
    return total if total else 0.0

# Check if expenses exceed the budget
def check_budget_status(user_id, category, start_date, end_date):
    """Checks if the total expenses exceed the budget for a category in a given period."""
    # Get the total expenses for the category
    total_expenses = get_total_expenses(user_id, category, start_date, end_date)

    # Retrieve the budget for the category
    budget = get_budget_by_category(user_id, category)
    if not budget:
        return "No budget set for this category."

    budget_limit = budget[3]  # The 4th item in the budget tuple is the limit (amount)
    
    # Compare the total expenses to the budget limit
    if total_expenses > budget_limit:
        return f"You have exceeded your budget for {category}! Total spent: {total_expenses}, Budget: {budget_limit}"
    else:
        return f"You are within your budget for {category}. Total spent: {total_expenses}, Budget: {budget_limit}"

# Generate an expense report for a given period
def generate_expense_report(user_id, start_date, end_date):
    """Generates an expense report for a specific period."""
    conn = connect_db()
    cursor = conn.cursor()

    query = '''
        SELECT category, SUM(amount) as total_spent
        FROM expenses
        WHERE user_id = ? AND date_added BETWEEN ? AND ?
        GROUP BY category
    '''
    cursor.execute(query, (user_id, start_date, end_date))

    report = cursor.fetchall()
    conn.close()

    if not report:
        return "No expenses found for the given period."

    # Format the report
    report_lines = [f"Expense report for {start_date} to {end_date}:"]
    for row in report:
        category, total_spent = row
        report_lines.append(f"- {category}: {total_spent}")

    return "\n".join(report_lines)

# Create tables when the bot starts
create_expenses_table()
create_budgets_table()

```
