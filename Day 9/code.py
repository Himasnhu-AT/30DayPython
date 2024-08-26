
# Day 9 code implementation in Python

import sys

def divide(a, b):
    try:
        result = int(a) / int(b)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day9.py <number1> <number2>")
    else:
        divide(sys.argv[1], sys.argv[2])

