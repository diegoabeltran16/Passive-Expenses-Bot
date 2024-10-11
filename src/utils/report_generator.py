# src/utils/report_generator.py

import sqlite3
import csv
import os
from fpdf import FPDF
from src.utils.lang import translate
from src.utils.shared import get_user_language  # Use the function to get user language

def fetch_expenses(conn, user_id, start_date=None, end_date=None, category=None):
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

def generate_text_report(conn, user_id, start_date=None, end_date=None, category=None):
    expenses = fetch_expenses(conn, user_id, start_date, end_date, category)
    if not expenses:
        return translate("no_report_data", get_user_language(user_id))

    report_lines = [translate("report_generated", get_user_language(user_id)) + "\n"]
    for exp in expenses:
        report_lines.append(f"ID: {exp[0]}, Amount: {exp[2]}, Description: {exp[3]}, Category: {exp[4]}, Date: {exp[5]}")
    report_lines.append("\n" + translate("total_expenses", get_user_language(user_id)).format(total=len(expenses)))

    return "\n".join(report_lines)

def generate_csv_report(conn, user_id, start_date=None, end_date=None, category=None, file_path='report.csv'):
    expenses = fetch_expenses(conn, user_id, start_date, end_date, category)
    if not expenses:
        return None

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'User ID', 'Amount', 'Description', 'Category', 'Date Added'])
        for exp in expenses:
            writer.writerow(exp)

    return file_path

def generate_pdf_report(conn, user_id, start_date=None, end_date=None, category=None, file_path='report.pdf'):
    expenses = fetch_expenses(conn, user_id, start_date, end_date, category)
    if not expenses:
        return None

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=translate("report_generated", get_user_language(user_id)), ln=True, align='C')
    pdf.ln(10)

    for exp in expenses:
        pdf.cell(0, 10, txt=f"ID: {exp[0]}, Amount: {exp[2]}, Description: {exp[3]}, Category: {exp[4]}, Date: {exp[5]}", ln=True)

    pdf.output(file_path)
    return file_path

def generate_report(conn, user_id, start_date=None, end_date=None, category=None, format='text', file_path=None):
    expenses = fetch_expenses(conn, user_id, start_date, end_date, category)

    if format == 'text':
        return generate_text_report(conn, user_id, start_date, end_date, category)
    elif format == 'csv':
        return generate_csv_report(conn, user_id, start_date, end_date, category, file_path or 'report.csv')
    elif format == 'pdf':
        return generate_pdf_report(conn, user_id, start_date, end_date, category, file_path or 'report.pdf')
    else:
        raise ValueError(translate("report_format_not_supported", get_user_language(user_id)).format(format=format))
