
# Day 6 - Dictionaries - Code File

# Creating a dictionary
student = {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Major: {student['major']}")

# Modifying values
student['age'] = 21
student['major'] = 'Software Engineering'
print(f"Updated Age: {student['age']}")
print(f"Updated Major: {student['major']}")

# Adding a new item
student['city'] = 'Cambridge'
print(f"City: {student['city']}")

# Deleting an item
del student['city']
print(student)

# Iterating through the dictionary
print("\nStudent Information:")
for key in student:
    print(f"{key}: {student[key]}")

# Iterating using items()
print("\nStudent Information (using items()):")
for key, value in student.items():
    print(f"{key}: {value}")


