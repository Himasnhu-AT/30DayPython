
# Day 3 code implementation in Python

import sys

# Get the number from command line argument
number = int(sys.argv[1])

# Check the number using if-else statements
if number > 0:
  print("Positive")
elif number < 0:
  print("Negative")
else:
  print("Zero")

