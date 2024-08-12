# Working with Sets

# Create a set named 'nums' with unique integer elements
nums = {1, 2, 3, 4}

# Create another set 'nums2' using the set() constructor with a tuple of integers
nums2 = set((1, 2, 3, 4))

# Print both sets to show their contents
print("nums:", nums)  # Output: nums: {1, 2, 3, 4}
print("nums2:", nums2)  # Output: nums2: {1, 2, 3, 4}

# Print the type of 'nums', which will be <class 'set'>
print("Type of 'nums':", type(nums))  # Output: Type of 'nums': <class 'set'>

# Print the number of items in 'nums'
print("Number of items in 'nums':", len(nums))  # Output: Number of items in 'nums': 4

# Demonstrate that sets do not allow duplicate elements
nums = {1, 2, 2, 3}  # The duplicate '2' is removed
print("After removing duplicates:", nums)  # Output: After removing duplicates: {1, 2, 3}

# Demonstrate that Boolean values are treated as integers (True is 1, False is 0)
nums = {1, True, 2, False, 3, 4, 0}  # True is considered as 1, False as 0
print("Set with Boolean values:", nums)  # Output: Set with Boolean values: {0, 1, 2, 3, 4}

# Check if a value is in a set
print("Is 2 in 'nums':", 2 in nums)  # Output: Is 2 in 'nums': True

# Note: Elements in a set cannot be accessed by index or key, as sets are unordered

# Add a new element to the set
nums.add(8)
print("After adding 8:", nums)  # Output: After adding 8: {0, 1, 2, 3, 4, 8}

# Create a new set 'morenums' and add its elements to 'nums'
morenums = {5, 6, 7}
nums.update(morenums)
print("After updating with 'morenums':", nums)  # Output: After updating with 'morenums': {0, 1, 2, 3, 4, 5, 6, 7, 8}

# 'update' can be used with lists, tuples, and dictionaries as well

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print("Union of 'one' and 'two':", mynewset)  # Output: Union of 'one' and 'two': {1, 2, 3, 5, 6, 7}

# Keep only elements that are in both sets (intersection)
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)  # Updates 'one' to keep only common elements
print("After intersection update:", one)  # Output: After intersection update: {2, 3}

# Keep all elements except those that are in both sets (symmetric difference)
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)  # Updates 'one' to keep only unique elements
print("After symmetric difference update:", one)  # Output: After symmetric difference update: {1, 4}
