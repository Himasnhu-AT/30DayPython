
# Python test cases for Day 14

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day14.py")

# Read the content of day14.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Test Cases for string methods
try:
    # 1. Check for the presence of "Hello" in the string
    if "Hello" not in file_content:
        raise AssertionError('"Hello" should be present in the string')

    # 2. Check if the string is converted to uppercase
    if "HELLO WORLD!" not in file_content:
        raise AssertionError("The string should be converted to uppercase")

    # 3. Check for the replacement of "World" with "Python"
    if "Hello Python!" not in file_content:
        raise AssertionError('"World" should be replaced with "Python"')

    # 4. Check for the formatted string with "CS50" inserted
    if "Welcome to CS50!" not in file_content:
        raise AssertionError('The formatted string should include "CS50"')

    # 5. Check for the correct index of "o" in the string
    if "The index of the first 'o' is: 4" not in file_content:
        raise AssertionError("The index of the first 'o' should be printed correctly")

    print("Day 14 string method tests passed successfully!")
except Exception as error:
    print("Day 14 tests failed!")
    print(str(error))
    sys.exit(1)

# Run the script and check the output
try:
    output = subprocess.check_output(["python", file_path], encoding="utf-8")
    print("Day 14 script execution successful!")
except Exception as error:
    print("Day 14 script execution failed!")
    print(str(error))
    sys.exit(1)

