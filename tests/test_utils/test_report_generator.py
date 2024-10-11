# tests/test_utils/test_report_generator.py

import unittest
import os
from src.utils.report_generator import generate_report
from src.utils.shared import set_user_language, get_user_language
from src.utils.db import connect_db
from src.utils.lang import translate

class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.conn = connect_db()
        self.user_id = 1
        self.start_date = "2024-01-01"
        self.end_date = "2024-12-31"
        self.category = "Food"

        # Set up the user language for testing
        self.default_language = "en"
        set_user_language(self.user_id, self.default_language)

    def tearDown(self):
        # Clean up generated report files if they exist
        for report_file in ['report.csv', 'report.pdf']:
            if os.path.exists(report_file):
                os.remove(report_file)
        self.conn.close()

    def test_set_and_get_user_language(self):
        # Test setting and getting user language
        set_user_language(self.user_id, "es")
        language = get_user_language(self.user_id)
        self.assertEqual(language, "es")

        # Reset to default
        set_user_language(self.user_id, self.default_language)

    def test_generate_text_report(self):
        # Test generating a text report
            set_user_language(self.user_id, "en")
            report = generate_report(self.conn, self.user_id, self.start_date, self.end_date, self.category, format='text')
    
         # Fetch the expected translation for the report header
            expected_report_header = translate("report_generated", language="en")
    
         # Assert that the translated header is in the report
            self.assertIn(expected_report_header, report)

    def test_generate_csv_report(self):
        # Test generating a CSV report
        set_user_language(self.user_id, "es")
        file_path = generate_report(self.conn, self.user_id, self.start_date, self.end_date, self.category, format='csv', file_path='report.csv')
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(file_path, 'report.csv')

    def test_generate_pdf_report(self):
        # Test generating a PDF report
        set_user_language(self.user_id, "en")
        file_path = generate_report(self.conn, self.user_id, self.start_date, self.end_date, self.category, format='pdf', file_path='report.pdf')
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(file_path, 'report.pdf')

    def test_translate_messages_in_reports(self):
        # Test that translations are correctly applied in reports
        set_user_language(self.user_id, "es")
        message = translate("report_generated", language="es")
        self.assertEqual(message, "Informe generado con éxito.")
        
        # Reset to default
        set_user_language(self.user_id, self.default_language)

if __name__ == '__main__':
    unittest.main()
