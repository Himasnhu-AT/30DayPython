
import os
import unittest

class FileHandlingTests(unittest.TestCase):

    def test_file_creation(self):
        """Check if a file is created and contains expected content."""
        file_path = "day7_output.txt"
        try:
            with open(file_path, "r") as f:
                content = f.read()
                self.assertEqual(content, "This is a test string written to the file.\n")
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_file_reading(self):
        """Check if the file is read correctly."""
        file_path = "day7_input.txt"
        try:
            with open(file_path, "r") as f:
                content = f.read()
                self.assertEqual(content, "This is a sample input string.\n")
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_file_appending(self):
        """Check if content is appended to an existing file."""
        file_path = "day7_output.txt"
        try:
            with open(file_path, "a") as f:
                f.write("This is appended content.\n")
            with open(file_path, "r") as f:
                content = f.read()
                self.assertEqual(content, "This is a test string written to the file.\nThis is appended content.\n")
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

if __name__ == '__main__':
    unittest.main()

