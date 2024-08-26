
import sqlite3

# Connect to the database (create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table called 'users'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

# Insert some data into the 'users' table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))

# Commit the changes to the database
conn.commit()

# Fetch all rows from the 'users' table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the fetched data
print("Users:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# Close the database connection
conn.close()

