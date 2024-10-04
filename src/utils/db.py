import sqlite3

def create_expenses_table(conn):
    """Creates the 'expenses' table in the database if it doesn't already exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

def create_budgets_table(conn):
    """Creates the 'budgets' table in the database if it doesn't already exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            "limit" REAL NOT NULL,
            period TEXT NOT NULL,
            start_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL
        )
    ''')
    conn.commit()

def insert_expense(conn, user_id, amount, description, category=None):
    """Inserts a new expense into the 'expenses' table."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (user_id, amount, description, category)
        VALUES (?, ?, ?, ?)
    ''', (user_id, amount, description, category))
    conn.commit()

def insert_budget(conn, user_id, category, limit, period, start_date, end_date):
    """Inserts a new budget into the 'budgets' table."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO budgets (user_id, category, "limit", period, start_date, end_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, category, limit, period, start_date, end_date))
    conn.commit()

def get_budget_by_category(conn, user_id, category):
    """Retrieves the budget for a specific category and user."""
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM budgets WHERE user_id = ? AND category = ?
    ''', (user_id, category))
    return cursor.fetchone()

def update_budget(conn, budget_id, new_limit):
    """Updates the limit of an existing budget."""
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE budgets
        SET "limit" = ?
        WHERE id = ?
    ''', (new_limit, budget_id))
    conn.commit()

def update_expense_category(conn, expense_id, category):
    """Updates the category of an existing expense."""
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE expenses
        SET category = ?
        WHERE id = ?
    ''', (category, expense_id))
    conn.commit()

def get_expenses_by_category(conn, user_id, category, start_date=None, end_date=None):
    """Retrieves all expenses by category for a specific user."""
    cursor = conn.cursor()
    query = 'SELECT * FROM expenses WHERE category = ? AND user_id = ?'
    params = [category, user_id]

    if start_date and end_date:
        query += ' AND date_added BETWEEN ? AND ?'
        params.extend([start_date, end_date])

    cursor.execute(query, params)
    return cursor.fetchall()

def connect_db():
    """
    Establishes a connection to the SQLite database.
    """
    return sqlite3.connect('expenses.db')  