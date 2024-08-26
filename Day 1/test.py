
# Python test cases for Day 1

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day1.py")

# Read the content of day1.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Regex pattern to check the variable assignment
greeting_pattern = r'greeting\s*=\s*"Hello, World!"'

try:
    # Ensure the greeting variable is assigned "Hello, World!"
    if not re.search(greeting_pattern, file_content):
        raise AssertionError('The greeting variable should be assigned "Hello, World!"')

    print("Day 1 variable assignment test passed successfully!")

    # Check the script's output
    output = subprocess.check_output(["python", file_path], encoding="utf-8")

    # Check that the output contains "Hello, World!"
    if "Hello, World!" not in output:
        raise AssertionError('The script should output "Hello, World!"')

    # Check that the output contains the value of the greeting variable ("Hello, World!")
    if "Hello, World!" not in output:
        raise AssertionError('The script should output the value of the greeting variable, "Hello, World!"')

    print("Day 1 output test passed successfully!")
except Exception as error:
    print("Day 1 tests failed!")
    print(str(error))
    sys.exit(1)

