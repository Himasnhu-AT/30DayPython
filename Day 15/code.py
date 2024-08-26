
# Day 15 code implementation in Python

import re

# Define test strings and patterns
test_string_one = "This is a test string."
pattern_one = r"test"

test_string_two = "This is another test string."
pattern_two = r"test\s+string"

test_string_three = "This is a test string with numbers 12345."
pattern_three = r"\d+"

test_string_four = "This is a test string with emails: test@example.com and another@example.com"
pattern_four = r"\S+@\S+\.\S+"

test_string_five = "This is a test string with no match."
pattern_five = r"nonexistent"

# Test the patterns against the strings
print(f"Is '{pattern_one}' present in '{test_string_one}': {bool(re.search(pattern_one, test_string_one))}")
print(f"Is '{pattern_two}' present in '{test_string_two}': {bool(re.search(pattern_two, test_string_two))}")
print(f"Is '{pattern_three}' present in '{test_string_three}': {bool(re.search(pattern_three, test_string_three))}")
print(f"Is '{pattern_four}' present in '{test_string_four}': {bool(re.search(pattern_four, test_string_four))}")
print(f"Is '{pattern_five}' present in '{test_string_five}': {bool(re.search(pattern_five, test_string_five))}")


