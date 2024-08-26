
# Day 14 code implementation in Python

# String operations
my_string = "Hello World!"

# 1. Check if a substring is present
if "Hello" in my_string:
    print("The substring 'Hello' is present")

# 2. Convert to uppercase
my_string = my_string.upper()
print(my_string)

# 3. Replace a substring
my_string = my_string.replace("World", "Python")
print(my_string)

# 4. Format a string
name = "CS50"
greeting = "Welcome to {}!"
print(greeting.format(name))

# 5. Find the index of a character
index = my_string.find("o")
print(f"The index of the first 'o' is: {index}")

