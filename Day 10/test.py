
# Python test cases for Day 10

import unittest

class TestDay10(unittest.TestCase):

    def test_class_creation(self):
        # Check if the Car class exists
        from day10 import Car
        self.assertTrue(hasattr(day10, 'Car'))

    def test_object_creation(self):
        # Check if an instance of Car can be created
        from day10 import Car
        car = Car("Red", 4)
        self.assertIsInstance(car, Car)

    def test_attribute_access(self):
        # Check if the attributes of the Car object are accessible
        from day10 import Car
        car = Car("Red", 4)
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.wheels, 4)

    def test_method_call(self):
        # Check if the honk method of the Car object works
        from day10 import Car
        car = Car("Red", 4)
        self.assertEqual(car.honk(), "Beep! Beep!")

if __name__ == '__main__':
    unittest.main()

