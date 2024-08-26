
# Day 13: Exploring data structures in Python

# Tuples - Immutable sequences
my_tuple = (1, 2, 3, "a", "b")

# Accessing elements
print(f"First element: {my_tuple[0]}")
print(f"Fourth element: {my_tuple[3]}")

# Trying to modify a tuple (raises an error)
# my_tuple[0] = 4  # This will cause an error

# Sets - Unordered collections of unique elements
my_set = {1, 2, 3, "a", "b"}

# Checking for membership
if 1 in my_set:
    print("1 is in the set")
else:
    print("1 is not in the set")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2
print(f"Union: {union_set}")

# Intersection
intersection_set = set1 & set2
print(f"Intersection: {intersection_set}")

# Difference
difference_set = set1 - set2
print(f"Difference: {difference_set}")

# Frozen sets - Immutable sets
my_frozenset = frozenset([1, 2, 3])

# Trying to modify a frozen set (raises an error)
# my_frozenset.add(4)  # This will cause an error

print(f"Frozen set: {my_frozenset}")

