
# Python test cases for Day 8

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day8.py")

# Read the content of day8.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Regex pattern to check the input() function usage
input_pattern = r'input\(\)'

try:
    # Ensure the input() function is used
    if not re.search(input_pattern, file_content):
        raise AssertionError('You need to use the input() function to get user input.')

    # Run the script and capture the output
    output = subprocess.check_output(["python", file_path], input="John Doe\n", encoding="utf-8")

    # Check if the output contains the expected message
    if "Hello, John Doe!" not in output:
        raise AssertionError("The output should include 'Hello, John Doe!'")

    print("Day 8 tests passed successfully!")

except Exception as error:
    print("Day 8 tests failed!")
    print(str(error))
    sys.exit(1)

