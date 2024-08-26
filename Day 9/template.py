
# /* DAY 9: Handling Exceptions
#  *
#  * Implement a function called `divide` that takes two numbers as input.
#  * Inside the `divide` function, use a `try-except` block to handle potential errors:
#  *   - Catch `ZeroDivisionError` if the user attempts to divide by zero.
#  *   - Catch `ValueError` if the user provides invalid input (non-numeric values).
#  *   - If no error occurs, calculate the result and print it.
#  *
#  * LICENSE: ALL RIGHTS RESERVED (C) 2024 @OpenEdu <git: openeduhq> @Himanshu <git: himanshu-at>
#  *
#  **/

import sys

def divide(a, b):
    # Write your code below this line

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day9.py <number1> <number2>")
    else:
        divide(sys.argv[1], sys.argv[2])
