import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
def connect_db():
    return sqlite3.connect('expenses.db')

# Initialize the expenses table
def create_expenses_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Add a new expense
def add_expense(amount, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO expenses (amount, description)
        VALUES (?, ?)
    ''', (amount, description))

    conn.commit()
    expense_id = cursor.lastrowid  # Get the ID of the inserted row
    conn.close()

    return expense_id  # Return the ID of the inserted row

# Delete an expense by ID
def delete_expense(expense_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))

    conn.commit()
    conn.close()

# List all expenses
def list_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT id, amount, description, date_added FROM expenses')
    expenses = cursor.fetchall()

    conn.close()

    return expenses  # Return a list of all expenses

# Update an existing expense by ID
def update_expense(expense_id, new_amount, new_description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE expenses
        SET amount = ?, description = ?
        WHERE id = ?
    ''', (new_amount, new_description, expense_id))

    conn.commit()
    conn.close()

# Call this function to create the table when the bot starts
create_expenses_table()
