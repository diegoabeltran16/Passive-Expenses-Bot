import sqlite3

def connect_db():
    """
    Establishes a connection to the SQLite database and creates necessary tables if they don't exist.
    Returns the database connection object.
    """
    try:
        conn = sqlite3.connect('src/database/expenses.db')
        create_expenses_table(conn)
        create_budgets_table(conn)
        create_user_language_table(conn)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_expenses_table(conn):
    """Creates the 'expenses' table in the database if it doesn't already exist."""
    try:
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
    except sqlite3.Error as e:
        print(f"Error creating expenses table: {e}")
        conn.rollback()

def create_budgets_table(conn):
    """Creates the 'budgets' table in the database if it doesn't already exist."""
    try:
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
    except sqlite3.Error as e:
        print(f"Error creating budgets table: {e}")
        conn.rollback()

def create_user_language_table(conn):
    """Creates the 'user_language' table in the database if it doesn't already exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_language (
                user_id INTEGER PRIMARY KEY,
                language TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating user_language table: {e}")
        conn.rollback()

def insert_expense(conn, user_id, amount, description, category=None):
    """Inserts a new expense into the 'expenses' table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (user_id, amount, description, category)
            VALUES (?, ?, ?, ?)
        ''', (user_id, amount, description, category))
        conn.commit()
        return cursor.lastrowid  # Return the ID of the newly inserted expense
    except sqlite3.Error as e:
        print(f"Error inserting expense: {e}")
        conn.rollback()
        return None

def delete_expense(conn, expense_id):
    """Deletes an expense by its ID."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM expenses WHERE id = ?
        ''', (expense_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting expense: {e}")
        conn.rollback()

def update_expense(conn, expense_id, new_amount, new_description):
    """Updates the amount and description of an existing expense."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE expenses
            SET amount = ?, description = ?
            WHERE id = ?
        ''', (new_amount, new_description, expense_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating expense: {e}")
        conn.rollback()

def update_expense_category(conn, expense_id, category):
    """Updates the category of an existing expense."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE expenses
            SET category = ?
            WHERE id = ?
        ''', (category, expense_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating expense category: {e}")
        conn.rollback()

def get_expenses_by_user(conn, user_id):
    """Retrieves all expenses for a specific user."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM expenses WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving expenses: {e}")
        return []

def get_expenses_by_category(conn, user_id, category, start_date=None, end_date=None):
    """Retrieves all expenses by category for a specific user."""
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM expenses WHERE category = ? AND user_id = ?'
        params = [category, user_id]

        if start_date and end_date:
            query += ' AND date_added BETWEEN ? AND ?'
            params.extend([start_date, end_date])

        cursor.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving expenses by category: {e}")
        return []

def list_expenses(conn, user_id):
    """Lists all expenses for a specific user."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM expenses WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error listing expenses: {e}")
        return []

def insert_budget(conn, user_id, category, limit, period, start_date, end_date):
    """Inserts a new budget into the 'budgets' table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO budgets (user_id, category, "limit", period, start_date, end_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, category, limit, period, start_date, end_date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting budget: {e}")
        conn.rollback()

def get_budget_by_category(conn, user_id, category):
    """Retrieves the budget for a specific category and user."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM budgets WHERE user_id = ? AND category = ?
        ''', (user_id, category))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error retrieving budget: {e}")
        return None

def update_budget(conn, budget_id, new_limit):
    """Updates the limit of an existing budget."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE budgets
            SET "limit" = ?
            WHERE id = ?
        ''', (new_limit, budget_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating budget: {e}")
        conn.rollback()

def insert_report(conn, user_id, filters, file_path):
    """
    Inserts a new report into the 'reports' table.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reports (user_id, filters, file_path)
            VALUES (?, ?, ?)
        ''', (user_id, filters, file_path))
        conn.commit()
        return cursor.lastrowid  # Return the ID of the newly inserted report
    except sqlite3.Error as e:
        print(f"Error inserting report: {e}")
        conn.rollback()
        return None

def get_reports_by_user(conn, user_id):
    """
    Retrieves all reports for a specific user.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM reports WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving reports: {e}")
        return []

def delete_report(conn, report_id):
    """
    Deletes a report by its ID.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM reports WHERE report_id = ?
        ''', (report_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting report: {e}")
        conn.rollback()

def create_reports_table(conn):
    """
    Creates the 'reports' table in the database if it doesn't already exist.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                report_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                filters TEXT,
                file_path TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating reports table: {e}")
        conn.rollback()
