
# Python test cases for Day 5

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day5.py")

# Define test cases
test_cases = [
    {
        "input": 5,
        "expected_output": 25,
        "function_name": "square_number"
    },
    {
        "input": "Hello",
        "expected_output": "HELLO",
        "function_name": "uppercase"
    },
    {
        "input": 10,
        "expected_output": 5,
        "function_name": "half_the_number"
    }
]

def run_test(test_case):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()

        # Check if the function definition exists
        function_pattern = rf'def {test_case["function_name"]}\(x\):'
        if not re.search(function_pattern, file_content):
            raise AssertionError(f"Function {test_case['function_name']} is not defined!")

        # Execute the function
        output = subprocess.check_output(
            ["python", file_path, str(test_case["input"])],
            encoding="utf-8"
        )

        # Remove newline characters from output
        output = output.strip()

        # Check the output
        if int(output) != test_case["expected_output"]:
            raise AssertionError(
                f"Function {test_case['function_name']} returned {output} instead of {test_case['expected_output']}."
            )

        print(f"Test for {test_case['function_name']} with input {test_case['input']} passed successfully!")
    except Exception as error:
        print(f"Test for {test_case['function_name']} failed!")
        print(str(error))
        sys.exit(1)

# Run tests for each function
for test_case in test_cases:
    run_test(test_case)

