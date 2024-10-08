import unittest
import sys
import os

# Add the 'src' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from utils.lang import translate

class TestTranslation(unittest.TestCase):

    def test_translation_to_english(self):
        """Test translating a message to English."""
        result = translate("expense_logged", "en", id=1, amount=100, description="Lunch")
        self.assertEqual(result, "Expense logged with ID 1: 100 for Lunch.")

    def test_translation_to_spanish(self):
        """Test translating a message to Spanish."""
        result = translate("expense_logged", "es", id=1, amount=100, description="Almuerzo")
        self.assertEqual(result, "Gasto registrado con ID 1: 100 por Almuerzo.")

    def test_invalid_translation_key(self):
        """Test handling of invalid translation keys."""
        result = translate("invalid_key", "en")
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
