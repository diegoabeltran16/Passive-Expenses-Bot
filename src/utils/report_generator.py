import sqlite3
import csv
import os
from fpdf import FPDF
from src.utils.lang import translate
from src.utils.shared import user_language

def fetch_expenses(conn, user_id, start_date=None, end_date=None, category=None):
    """
    Fetch expenses from the database based on filters.

    :param conn: SQLite connection object
    :param user_id: ID of the user
    :param start_date: (Optional) Start date for filtering expenses
    :param end_date: (Optional) End date for filtering expenses
    :param category: (Optional) Category for filtering expenses
    :return: A list of tuples containing expense data
    """
    cursor = conn.cursor()
    query = '''
        SELECT id, user_id, amount, description, category, date_added
        FROM expenses
        WHERE user_id = ?
    '''
    params = [user_id]

    if start_date:
        query += ' AND date_added >= ?'
        params.append(start_date)
    if end_date:
        query += ' AND date_added <= ?'
        params.append(end_date)
    if category:
        query += ' AND category = ?'
        params.append(category)

    cursor.execute(query, tuple(params))
    return cursor.fetchall()

def generate_text_report(expenses):
    """
    Generate a plain text report from expense data.

    :param expenses: A list of expense tuples
    :return: A string containing the report
    """
    if not expenses:
        return "No expenses found for the given filters."

    report_lines = ["Expense Report:\n"]
    for exp in expenses:
        report_lines.append(f"ID: {exp[0]}, Amount: {exp[2]}, Description: {exp[3]}, Category: {exp[4]}, Date: {exp[5]}")
    report_lines.append("\nTotal Expenses: " + str(len(expenses)))

    return "\n".join(report_lines)

def generate_csv_report(expenses, file_path='report.csv'):
    """
    Generate a CSV report from expense data.

    :param expenses: A list of expense tuples
    :param file_path: The file path to save the CSV report
    :return: The path to the generated CSV file
    """
    if not expenses:
        return None

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'User ID', 'Amount', 'Description', 'Category', 'Date Added'])
        for exp in expenses:
            writer.writerow(exp)

    return file_path

def generate_pdf_report(expenses, file_path='report.pdf'):
    """
    Generate a PDF report from expense data.

    :param expenses: A list of expense tuples
    :param file_path: The file path to save the PDF report
    :return: The path to the generated PDF file
    """
    if not expenses:
        return None

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Expense Report", ln=True, align='C')
    pdf.ln(10)

    for exp in expenses:
        pdf.cell(0, 10, txt=f"ID: {exp[0]}, Amount: {exp[2]}, Description: {exp[3]}, Category: {exp[4]}, Date: {exp[5]}", ln=True)

    pdf.output(file_path)
    return file_path

def generate_report(conn, user_id, start_date=None, end_date=None, category=None, format='text', file_path=None):
    """
    Generate a report based on user filters and the specified format.

    :param conn: SQLite connection object
    :param user_id: ID of the user for whom the report is generated
    :param start_date: (Optional) Start date for filtering expenses
    :param end_date: (Optional) End date for filtering expenses
    :param category: (Optional) Category for filtering expenses
    :param format: Report format ('text', 'csv', 'pdf')
    :param file_path: Optional path for saving the report (for CSV/PDF)
    :return: The report as a string (for text) or a file path (for CSV/PDF)
    """
    expenses = fetch_expenses(conn, user_id, start_date, end_date, category)

    if format == 'text':
        return generate_text_report(expenses)
    elif format == 'csv':
        return generate_csv_report(expenses, file_path or 'report.csv')
    elif format == 'pdf':
        return generate_pdf_report(expenses, file_path or 'report.pdf')
    else:
        raise ValueError("Invalid format. Supported formats are: 'text', 'csv', 'pdf'.")
