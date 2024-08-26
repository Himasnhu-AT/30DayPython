
# Python test cases for Day 29

import os
import unittest

# Define a custom exception for testing purposes
class InvalidInputError(Exception):
    pass

class Day29Test(unittest.TestCase):

    def test_data_structures(self):
        # Test list manipulation
        self.assertEqual(len([1, 2, 3, 4, 5]), 5)
        self.assertIn(3, [1, 2, 3, 4, 5])
        self.assertNotIn(6, [1, 2, 3, 4, 5])

        # Test dictionary usage
        my_dict = {"name": "John", "age": 30}
        self.assertEqual(my_dict["name"], "John")
        self.assertEqual(my_dict.get("age"), 30)

        # Test tuple immutability
        my_tuple = (1, 2, 3)
        with self.assertRaises(TypeError):
            my_tuple[0] = 4

    def test_control_flow(self):
        # Test if-else conditional statement
        def check_age(age):
            if age >= 18:
                return "Adult"
            else:
                return "Minor"

        self.assertEqual(check_age(25), "Adult")
        self.assertEqual(check_age(15), "Minor")

        # Test for loop iteration
        sum = 0
        for i in range(1, 6):
            sum += i
        self.assertEqual(sum, 15)

        # Test while loop condition
        count = 0
        while count < 5:
            count += 1
        self.assertEqual(count, 5)

    def test_functions(self):
        # Test function definition and invocation
        def greet(name):
            return "Hello, " + name + "!"

        self.assertEqual(greet("Alice"), "Hello, Alice!")

        # Test function parameters and return values
        def add_numbers(x, y):
            return x + y

        self.assertEqual(add_numbers(5, 7), 12)

    def test_oop(self):
        # Test class definition and instantiation
        class Dog:
            def __init__(self, name, breed):
                self.name = name
                self.breed = breed

            def bark(self):
                return "Woof!"

        my_dog = Dog("Buddy", "Golden Retriever")
        self.assertEqual(my_dog.name, "Buddy")
        self.assertEqual(my_dog.breed, "Golden Retriever")
        self.assertEqual(my_dog.bark(), "Woof!")

    def test_file_handling(self):
        # Test file writing and reading
        file_path = "day29_test.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("This is a test file.")

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, "This is a test file.")

        os.remove(file_path)  # Clean up the test file

    def test_exception_handling(self):
        # Test handling a custom exception
        def divide(x, y):
            if y == 0:
                raise InvalidInputError("Cannot divide by zero.")
            return x / y

        with self.assertRaises(InvalidInputError):
            divide(10, 0)

        self.assertEqual(divide(10, 2), 5.0)

    def test_modules_and_packages(self):
        # Test importing and using a module
        import math

        self.assertEqual(math.sqrt(25), 5.0)
        self.assertEqual(math.pi, 3.141592653589793)

# Run the tests
if __name__ == '__main__':
    unittest.main()

