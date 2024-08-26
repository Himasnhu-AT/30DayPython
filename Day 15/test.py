
# Python test cases for Day 15

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day15.py")

# Define test cases
test_cases = [
    ("test_string_one", "This is a test string.", r"test", True),
    ("test_string_two", "This is another test string.", r"test\s+string", True),
    ("test_string_three", "This is a test string with numbers 12345.", r"\d+", True),
    ("test_string_four", "This is a test string with emails: test@example.com and another@example.com", r"\S+@\S+\.\S+", True),
    ("test_string_five", "This is a test string with no match.", r"nonexistent", False),
]

# Run tests
for test_name, test_string, pattern, expected_result in test_cases:
    try:
        # Read the content of day15.py
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()

        # Check if the regex pattern is present in the file
        if re.search(pattern, file_content):
            # Check if the script's output matches the expected result
            output = subprocess.check_output(["python", file_path], encoding="utf-8")
            output = output.strip().split("\n")[-1]  # Get the last line of output
            if output == str(expected_result):
                print(f"{test_name} passed!")
            else:
                raise AssertionError(
                    f"{test_name} failed! Expected '{expected_result}' but got '{output}'"
                )
        else:
            raise AssertionError(f"{test_name} failed! Regex pattern not found in the code.")
    except Exception as error:
        print(f"{test_name} failed!")
        print(str(error))
        sys.exit(1)

