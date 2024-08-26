
# Day 7 code implementation in Python

# Writing to a file
with open("day7_output.txt", "w") as file:
    file.write("This is a test string written to the file.\n")

# Reading from a file
with open("day7_input.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("day7_output.txt", "a") as file:
    file.write("This is appended content.\n")

