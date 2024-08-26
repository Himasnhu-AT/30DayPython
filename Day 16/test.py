
import unittest

class LambdaFunctionTests(unittest.TestCase):

    def test_square_function(self):
        square = lambda x: x * x
        self.assertEqual(square(5), 25)

    def test_addition_function(self):
        add_five = lambda x: x + 5
        self.assertEqual(add_five(10), 15)

    def test_sort_list(self):
        numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        sorted_numbers = sorted(numbers, key=lambda x: x)
        self.assertEqual(sorted_numbers, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_filter_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
        self.assertEqual(even_numbers, [2, 4, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()

