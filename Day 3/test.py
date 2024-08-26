
# Python test cases for Day 3

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day3.py")

# Read the content of day3.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Test case 1: Check if the code handles a positive number correctly
try:
    output = subprocess.check_output(["python", file_path, "5"], encoding="utf-8")
    if output.strip() != "Positive":
        raise AssertionError("Test case 1 failed: Incorrect output for positive number.")
    print("Test case 1 passed successfully!")
except Exception as error:
    print("Test case 1 failed!")
    print(str(error))

# Test case 2: Check if the code handles a negative number correctly
try:
    output = subprocess.check_output(["python", file_path, "-5"], encoding="utf-8")
    if output.strip() != "Negative":
        raise AssertionError("Test case 2 failed: Incorrect output for negative number.")
    print("Test case 2 passed successfully!")
except Exception as error:
    print("Test case 2 failed!")
    print(str(error))

# Test case 3: Check if the code handles zero correctly
try:
    output = subprocess.check_output(["python", file_path, "0"], encoding="utf-8")
    if output.strip() != "Zero":
        raise AssertionError("Test case 3 failed: Incorrect output for zero.")
    print("Test case 3 passed successfully!")
except Exception as error:
    print("Test case 3 failed!")
    print(str(error))

