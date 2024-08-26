
import sqlite3
import unittest

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_create_student(self):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 20))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM students WHERE name = 'Alice'")
        result = self.cursor.fetchone()
        self.assertEqual(result[1], "Alice")
        self.assertEqual(result[2], 20)

    def test_update_student_age(self):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 22))
        self.conn.commit()
        self.cursor.execute("UPDATE students SET age = 25 WHERE name = 'Bob'")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM students WHERE name = 'Bob'")
        result = self.cursor.fetchone()
        self.assertEqual(result[2], 25)

    def test_delete_student(self):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Charlie", 21))
        self.conn.commit()
        self.cursor.execute("DELETE FROM students WHERE name = 'Charlie'")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM students WHERE name = 'Charlie'")
        result = self.cursor.fetchone()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

