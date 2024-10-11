# tests/test_utils/test_report_generator.py

import unittest
from src.utils.shared import set_user_language, get_user_language

class TestSharedUtilities(unittest.TestCase):

    def test_set_user_language(self):
        user_id = 1
        language = "es"
        set_user_language(user_id, language)
        self.assertEqual(get_user_language(user_id), language)

if __name__ == '__main__':
    unittest.main()
