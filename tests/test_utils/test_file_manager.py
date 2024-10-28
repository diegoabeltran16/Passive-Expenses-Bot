import unittest
import os
from src.utils.file_manager import save_file, read_file, delete_file
from src.utils.shared import set_user_language

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.language = 'en'
        set_user_language(self.user_id, self.language)

        self.directory = 'test_reports'
        self.filename = 'test_file.txt'
        self.file_path = os.path.join(self.directory, self.filename)
        self.content = b'This is a test file.'

    def tearDown(self):
        # Clean up test directory and files if they exist
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.directory):
            os.rmdir(self.directory)

    def test_save_file(self):
        # Test saving a file
        result = save_file(self.content, self.directory, self.filename, self.user_id)
        self.assertEqual(result, f"File saved at: {self.file_path}.")
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_file(self):
        # Save a file first, then read it
        save_file(self.content, self.directory, self.filename, self.user_id)
        message, result = read_file(self.file_path, self.user_id)
        self.assertEqual(message, f"File retrieved: {self.file_path}.")
        self.assertEqual(result, self.content)

    def test_delete_file(self):
        # Save a file first, then delete it
        save_file(self.content, self.directory, self.filename, self.user_id)
        result = delete_file(self.file_path, self.user_id)
        self.assertEqual(result, "File deleted successfully.")
        self.assertFalse(os.path.exists(self.file_path))

if __name__ == '__main__':
    unittest.main()
