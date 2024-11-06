#src\utils\generate_report.py

import csv
import os
import logging

def generate_report(conn, user_id, start_date=None, end_date=None, category=None, format="csv", file_path=None):
    """
    Generates an expense report in the specified format based on filters.
    """
    # SQL query with date filters and handling NULL categories
    query = "SELECT amount, description, category, date(date_added) FROM expenses WHERE user_id = ?"
    params = [user_id]

    if start_date:
        query += " AND date(date_added) >= date(?)"
        params.append(start_date)
    if end_date:
        query += " AND date(date_added) <= date(?)"
        params.append(end_date)
    if category:
        query += " AND category IS NOT NULL AND LOWER(category) = LOWER(?)"
        params.append(category)

    # Log the query and parameters
    logging.info(f"Executing query: {query} with parameters: {params}")

    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    expenses = cursor.fetchall()

    # Handle empty results
    if not expenses:
        logging.info("No data found for the specified parameters.")
        return None if format == "csv" else ""

    # Generate report based on format
    if format == "text":
        return generate_text_report(expenses)
    elif format == "csv" and file_path:
        return generate_csv_report(expenses, file_path)
    else:
        raise ValueError("Unsupported report format.")

def generate_text_report(expenses):
    report = "Expense Report\n\n"
    for amount, description, category, date_added in expenses:
        report += f"Amount: {amount}, Description: {description}, Category: {category if category else 'N/A'}, Date Added: {date_added}\n"
    return report

def generate_csv_report(expenses, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Description", "Category", "Date Added"])
        for expense in expenses:
            writer.writerow(expense)
    
    logging.info(f"CSV report saved to {file_path}")
    return file_path
