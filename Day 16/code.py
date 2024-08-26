
# Day 16: Lambda Functions in Python

# Define a lambda function to square a number
square = lambda x: x * x

# Calculate the square of 5
result = square(5)
print(f"Square of 5: {result}")

# Define a lambda function to add 5 to a number
add_five = lambda x: x + 5

# Add 5 to 10
result = add_five(10)
print(f"10 + 5: {result}")

# Sort a list of numbers using a lambda function as the key
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(f"Sorted numbers: {sorted_numbers}")

# Filter even numbers from a list using a lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

