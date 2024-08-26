
import sqlite3

# Connect to the database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
conn.commit()

# Insert new student records
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 21)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Charlie', 23)")
conn.commit()

# Retrieve all student records
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
print("All students:")
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Update a student's age
cursor.execute("UPDATE students SET age = 24 WHERE name = 'Charlie'")
conn.commit()

# Retrieve the updated student record
cursor.execute("SELECT * FROM students WHERE name = 'Charlie'")
result = cursor.fetchone()
print(f"\nUpdated Charlie's age: {result[2]}")

# Delete a student record
cursor.execute("DELETE FROM students WHERE name = 'Bob'")
conn.commit()

# Retrieve all student records again
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
print("\nStudents after deleting Bob:")
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Close the database connection
cursor.close()
conn.close()

