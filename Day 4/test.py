
# Python test cases for Day 4

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day4.py")

# Read the content of day1.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Test Case 1: For loop - iterate through a list and print each item
try:
    # Check if the for loop exists
    for_loop_pattern = r"for\s+item\s+in\s+my_list\s*:\s*"
    if not re.search(for_loop_pattern, file_content):
        raise AssertionError("For loop for iterating over my_list not found.")

    # Check if printing the item exists
    print_item_pattern = r"print\s*\(\s*item\s*\)"
    if not re.search(print_item_pattern, file_content):
        raise AssertionError("Printing item inside the for loop not found.")

    # Run the code and check the output
    output = subprocess.check_output(["python", file_path], encoding="utf-8").strip()
    expected_output = "1\n2\n3\n4\n5"
    if output != expected_output:
        raise AssertionError(f"Incorrect output: expected '{expected_output}' but got '{output}'")

    print("Test Case 1: For loop iteration passed!")
except Exception as error:
    print("Test Case 1 failed!")
    print(str(error))

# Test Case 2: While loop - count to 5
try:
    # Check if the while loop exists
    while_loop_pattern = r"while\s+counter\s+<\s+5\s*:"
    if not re.search(while_loop_pattern, file_content):
        raise AssertionError("While loop for counting to 5 not found.")

    # Check if incrementing counter exists
    increment_counter_pattern = r"counter\s*=\s*counter\s*\+\s*1"
    if not re.search(increment_counter_pattern, file_content):
        raise AssertionError("Incrementing the counter inside the while loop not found.")

    # Check if printing the counter exists
    print_counter_pattern = r"print\s*\(\s*counter\s*\)"
    if not re.search(print_counter_pattern, file_content):
        raise AssertionError("Printing the counter inside the while loop not found.")

    # Run the code and check the output
    output = subprocess.check_output(["python", file_path], encoding="utf-8").strip()
    expected_output = "1\n2\n3\n4\n5"
    if output != expected_output:
        raise AssertionError(f"Incorrect output: expected '{expected_output}' but got '{output}'")

    print("Test Case 2: While loop counting passed!")
except Exception as error:
    print("Test Case 2 failed!")
    print(str(error))

