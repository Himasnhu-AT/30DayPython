
import sqlite3
import unittest

class TestDatabaseQueries(unittest.TestCase):

    def setUp(self):
        """Setup for database connection and table creation"""
        self.conn = sqlite3.connect('test_database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        """Close the database connection"""
        self.cursor.close()
        self.conn.close()

    def test_insert_student(self):
        """Test inserting a new student record"""
        self.cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM students WHERE name = 'Alice'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Alice')

    def test_select_all_students(self):
        """Test selecting all student records"""
        self.cursor.execute("SELECT * FROM students")
        results = self.cursor.fetchall()
        self.assertGreaterEqual(len(results), 0)

    def test_update_student_age(self):
        """Test updating a student's age"""
        self.cursor.execute("UPDATE students SET age = 22 WHERE name = 'Alice'")
        self.conn.commit()
        self.cursor.execute("SELECT age FROM students WHERE name = 'Alice'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 22)

    def test_delete_student(self):
        """Test deleting a student record"""
        self.cursor.execute("DELETE FROM students WHERE name = 'Alice'")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM students WHERE name = 'Alice'")
        result = self.cursor.fetchone()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

