
# Day 29 code implementation in Python

# Data Structures
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "John", "age": 30}
my_tuple = (1, 2, 3)
my_set = {1, 2, 3, 4, 5}

# Control Flow
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Functions
def greet(name):
    return "Hello, " + name + "!"

# Object-Oriented Programming (OOP)
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

# File Handling
with open("day29.txt", "w", encoding="utf-8") as file:
    file.write("This is a test file.")

with open("day29.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Exception Handling
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

try:
    result = divide(10, 0)
except ZeroDivisionError as error:
    print(error)

# Modules and Packages
import math

print(math.sqrt(25))
print(math.pi)

