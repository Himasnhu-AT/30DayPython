
# /* DAY 15: Let's explore the power of Regular Expressions.
#  *
#  * We'll learn about regular expression syntax and apply them to pattern matching and text extraction.
#  *
#  * Create code to test five different patterns against five given strings. Use Python's 're' module and print the output in the specified format.
#  *
#  * LICENSE: ALL RIGHTS RESERVED (C) 2024 @OpenEdu <git: openeduhq> @Himanshu <git: himanshu-at>
#  *
#  **/

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

# Write your code below this line

# Test the patterns against the strings
print(f"Is '{pattern_one}' present in '{test_string_one}': ")
print(f"Is '{pattern_two}' present in '{test_string_two}': ")
print(f"Is '{pattern_three}' present in '{test_string_three}': ")
print(f"Is '{pattern_four}' present in '{test_string_four}': ")
print(f"Is '{pattern_five}' present in '{test_string_five}': ")
