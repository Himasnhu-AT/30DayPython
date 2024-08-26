
import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day12.py")

# Read the content of day12.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Regex pattern to check the import statement
import_pattern = r'import\s+random'

# Check for the import statement
try:
    if not re.search(import_pattern, file_content):
        raise AssertionError('The code should import the "random" module.')

    print("Day 12 module import test passed!")

    # Execute the script and capture output
    output = subprocess.check_output(["python", file_path], encoding="utf-8")

    # Regex pattern to check if the output contains the generated random number
    random_number_pattern = r'\d+'

    # Check for the random number in the output
    if not re.search(random_number_pattern, output):
        raise AssertionError('The code should print a random number.')

    print("Day 12 random number generation test passed!")

except Exception as error:
    print("Day 12 tests failed!")
    print(str(error))
    sys.exit(1)

