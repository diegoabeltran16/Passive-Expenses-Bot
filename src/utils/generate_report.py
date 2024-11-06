import csv
import os
import sqlite3

def generate_report(conn, user_id, start_date=None, end_date=None, category=None, format="csv", file_path=None):
    """
    Generates an expense report in the specified format based on filters.
    
    Parameters:
    - conn: SQLite database connection.
    - user_id: The ID of the user for whom to generate the report.
    - start_date: Filter for the start date.
    - end_date: Filter for the end date.
    - category: Filter for the category.
    - format: Format of the report ("csv" or "text").
    - file_path: Path to save the report if applicable (for CSV format).
    
    Returns:
    - For text format: Returns the report as a string.
    - For CSV: Returns the file path.
    """
    # Define SQL query with filters
    query = "SELECT amount, description, category, date_added FROM expenses WHERE user_id = ?"
    params = [user_id]

    if start_date:
        query += " AND date_added >= ?"
        params.append(start_date)
    if end_date:
        query += " AND date_added <= ?"
        params.append(end_date)
    if category:
        query += " AND category = ?"
        params.append(category)

    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    expenses = cursor.fetchall()

    # Return None if there are no expenses for the specified filters
    if not expenses:
        return None

    # Generate the report based on the specified format
    if format == "text":
        return generate_text_report(expenses)
    elif format == "csv" and file_path:
        return generate_csv_report(expenses, file_path)
    else:
        raise ValueError("Unsupported report format.")

def generate_text_report(expenses):
    """
    Generates a text report as a string.
    """
    report = "Expense Report\n\n"
    for amount, description, category, date_added in expenses:
        report += f"Amount: {amount}, Description: {description}, Category: {category if category else 'N/A'}, Date Added: {date_added}\n"
    return report

def generate_csv_report(expenses, file_path):
    """
    Generates a CSV report and saves it to file_path.
    """
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Description", "Category", "Date Added"])
        for expense in expenses:
            writer.writerow(expense)
    return file_path
