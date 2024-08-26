
# Python test cases for Day 9

import os
import subprocess
import re
import sys

file_path = os.path.join(os.path.dirname(__file__), "day9.py")

def test_divide_by_zero():
    try:
        output = subprocess.check_output(["python", file_path, "10", "0"], encoding="utf-8")
        assert False, "Should have raised a ZeroDivisionError"
    except subprocess.CalledProcessError as e:
        assert "ZeroDivisionError" in str(e.stderr), "Should have printed ZeroDivisionError message"

def test_invalid_input():
    try:
        output = subprocess.check_output(["python", file_path, "a", "b"], encoding="utf-8")
        assert False, "Should have raised a ValueError"
    except subprocess.CalledProcessError as e:
        assert "ValueError" in str(e.stderr), "Should have printed ValueError message"

def test_valid_division():
    try:
        output = subprocess.check_output(["python", file_path, "10", "2"], encoding="utf-8")
        assert "Result: 5.0" in output, "Should have printed the correct result"
    except subprocess.CalledProcessError as e:
        assert False, "Should not have raised an error"

if __name__ == "__main__":
    test_divide_by_zero()
    test_invalid_input()
    test_valid_division()
    print("All Day 9 tests passed successfully!")

