
# Python test cases for Day 13

import unittest

class TestDay13(unittest.TestCase):

    def test_tuple_creation(self):
        # Create a tuple
        my_tuple = (1, 2, 3, 'a', 'b')
        self.assertEqual(my_tuple, (1, 2, 3, 'a', 'b'))

    def test_tuple_access(self):
        my_tuple = (1, 2, 3, 'a', 'b')
        self.assertEqual(my_tuple[0], 1)
        self.assertEqual(my_tuple[3], 'a')

    def test_tuple_immutable(self):
        my_tuple = (1, 2, 3)
        with self.assertRaises(TypeError):
            my_tuple[0] = 4

    def test_set_creation(self):
        my_set = {1, 2, 3, 'a', 'b'}
        self.assertIn(1, my_set)
        self.assertIn('b', my_set)

    def test_set_operations(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        
        # Union
        union_set = set1 | set2 
        self.assertEqual(union_set, {1, 2, 3, 4, 5})
        
        # Intersection
        intersection_set = set1 & set2
        self.assertEqual(intersection_set, {3})
        
        # Difference
        difference_set = set1 - set2
        self.assertEqual(difference_set, {1, 2})

    def test_frozenset_creation(self):
        my_frozenset = frozenset([1, 2, 3])
        self.assertEqual(my_frozenset, frozenset([1, 2, 3]))

    def test_frozenset_immutable(self):
        my_frozenset = frozenset([1, 2, 3])
        with self.assertRaises(AttributeError):
            my_frozenset.add(4)

if __name__ == '__main__':
    unittest.main()

