
# Day 17 Python Test Cases

import unittest
from datetime import datetime

class TestDay17(unittest.TestCase):

    def test_current_date_time(self):
        """Checks if the code correctly retrieves the current date and time."""
        try:
            # Call the function to retrieve the current date and time
            current_datetime = get_current_datetime()

            # Ensure the retrieved object is a datetime object
            self.assertIsInstance(current_datetime, datetime)

            # Check if the current date and time are within a reasonable range
            # (You can adjust the range based on the expected behavior of your code)
            self.assertGreaterEqual(current_datetime.year, 2020)
            self.assertLessEqual(current_datetime.year, 2030)
        except Exception as e:
            self.fail(f"Error: {e}")

    def test_parse_datetime(self):
        """Checks if the code correctly parses a string to a datetime object."""
        try:
            # Call the function to parse the string
            parsed_datetime = parse_datetime("2024-02-15T12:34:56")

            # Ensure the retrieved object is a datetime object
            self.assertIsInstance(parsed_datetime, datetime)

            # Verify the date and time components
            self.assertEqual(parsed_datetime.year, 2024)
            self.assertEqual(parsed_datetime.month, 2)
            self.assertEqual(parsed_datetime.day, 15)
            self.assertEqual(parsed_datetime.hour, 12)
            self.assertEqual(parsed_datetime.minute, 34)
            self.assertEqual(parsed_datetime.second, 56)
        except Exception as e:
            self.fail(f"Error: {e}")

    def test_format_datetime(self):
        """Checks if the code correctly formats a datetime object as a string."""
        try:
            # Call the function to format the datetime object
            formatted_datetime = format_datetime(datetime(2024, 2, 15, 12, 34, 56), "%Y-%m-%dT%H:%M:%S")

            # Ensure the formatted string matches the expected format
            self.assertEqual(formatted_datetime, "2024-02-15T12:34:56")
        except Exception as e:
            self.fail(f"Error: {e}")

    def test_add_days(self):
        """Checks if the code correctly adds days to a datetime object."""
        try:
            # Call the function to add days
            new_datetime = add_days(datetime(2024, 2, 15), 3)

            # Verify the new date is 3 days later
            self.assertEqual(new_datetime.year, 2024)
            self.assertEqual(new_datetime.month, 2)
            self.assertEqual(new_datetime.day, 18)
        except Exception as e:
            self.fail(f"Error: {e}")

if __name__ == "__main__":
    unittest.main()

