
# Python test cases for Day 2

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day2.py")

# Read the content of day2.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Regex pattern to check string manipulation
string_manipulation_pattern = r"print\(sentence\[:5]\)"

try:
    # Ensure string manipulation is present
    if not re.search(string_manipulation_pattern, file_content):
        raise AssertionError('The code should include a line to print the first 5 characters of the sentence.')

    print("Day 2 string manipulation test passed successfully!")

    # Check the script's output
    output = subprocess.check_output(["python", file_path], encoding="utf-8")

    # Check for the first 5 characters of the sentence
    if "Hello" not in output:
        raise AssertionError('The output should include the first 5 characters of the sentence, "Hello".')

    print("Day 2 string manipulation output test passed successfully!")

    # Regex pattern to check list operations
    list_operations_pattern = r"print\(numbers\[2]\)"
    if not re.search(list_operations_pattern, file_content):
        raise AssertionError('The code should include a line to print the element at index 2 of the list.')

    print("Day 2 list operations test passed successfully!")

    # Check the script's output
    output = subprocess.check_output(["python", file_path], encoding="utf-8")

    # Check for the element at index 2 of the list
    if "3" not in output:
        raise AssertionError('The output should include the element at index 2 of the list, "3".')

    print("Day 2 list operations output test passed successfully!")

    # Regex pattern to check list manipulation (removing an element)
    list_manipulation_pattern = r"numbers\.remove\(3\)"
    if not re.search(list_manipulation_pattern, file_content):
        raise AssertionError('The code should include a line to remove the element "3" from the list.')

    print("Day 2 list manipulation test passed successfully!")

    # Check the script's output
    output = subprocess.check_output(["python", file_path], encoding="utf-8")

    # Check for the modified list output
    if "3" in output:
        raise AssertionError('The output should not include the element "3" after it has been removed from the list.')

    print("Day 2 list manipulation output test passed successfully!")

except Exception as error:
    print("Day 2 tests failed!")
    print(str(error))
    sys.exit(1)

