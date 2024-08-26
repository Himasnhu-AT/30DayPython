
# Day 6 - Dictionaries Test Cases

import unittest

class DictionaryTests(unittest.TestCase):

    def test_create_dictionary(self):
        """
        Test creating a basic dictionary.
        """
        student = {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
        self.assertEqual(student['name'], 'Alice')
        self.assertEqual(student['age'], 20)
        self.assertEqual(student['major'], 'Computer Science')

    def test_access_values(self):
        """
        Test accessing values from a dictionary.
        """
        student = {'name': 'Bob', 'age': 22, 'major': 'Math'}
        self.assertEqual(student['name'], 'Bob')
        self.assertEqual(student['age'], 22)
        self.assertEqual(student['major'], 'Math')

    def test_modify_values(self):
        """
        Test modifying values in a dictionary.
        """
        student = {'name': 'Charlie', 'age': 21, 'major': 'Physics'}
        student['age'] = 23
        student['major'] = 'Chemistry'
        self.assertEqual(student['age'], 23)
        self.assertEqual(student['major'], 'Chemistry')

    def test_add_items(self):
        """
        Test adding new items to a dictionary.
        """
        student = {'name': 'David', 'age': 24}
        student['major'] = 'Biology'
        self.assertEqual(student['major'], 'Biology')

    def test_delete_items(self):
        """
        Test deleting items from a dictionary.
        """
        student = {'name': 'Emily', 'age': 25, 'major': 'Psychology'}
        del student['major']
        self.assertNotIn('major', student)

    def test_iterate_through_dictionary(self):
        """
        Test iterating through a dictionary using keys.
        """
        student = {'name': 'Frank', 'age': 26, 'major': 'History'}
        for key in student:
            print(f"{key}: {student[key]}")
        # Check if the output is as expected.

    def test_iterate_through_dictionary_items(self):
        """
        Test iterating through a dictionary using items().
        """
        student = {'name': 'Grace', 'age': 27, 'major': 'Literature'}
        for key, value in student.items():
            print(f"{key}: {value}")
        # Check if the output is as expected.

if __name__ == '__main__':
    unittest.main()


