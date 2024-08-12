# Creating and manipulating lists

# Initialize a list of user names
users = ['Dave', 'John', 'Sara']

# Initialize a list with mixed data types
data = ['Dave', 42, True]

# Create an empty list
emptylist = []

# Check if 'Dave' is in the empty list (should return False)
print("Dave" in emptylist)

# Access the first element of the 'users' list
print(users[0])  # Output: 'Dave'

# Access the second-to-last element of the 'users' list
print(users[-2])  # Output: 'John'

# Find the index of 'Sara' in the 'users' list
print(users.index('Sara'))  # Output: 2

# Slice the first two elements of the 'users' list
print(users[0:2])  # Output: ['Dave', 'John']

# Slice from the second element to the end of the 'users' list
print(users[1:])  # Output: ['John', 'Sara']

# Slice from the third-to-last element to the second-to-last element
print(users[-3:-1])  # Output: ['Dave', 'John']

# Get the number of elements in the 'data' list
print(len(data))  # Output: 3

# Append a new element 'Elsa' to the 'users' list
users.append('Elsa')
print(users)  # Output: ['Dave', 'John', 'Sara', 'Elsa']

# Concatenate the list ['Jason'] to the 'users' list
users += ['Jason']
print(users)  # Output: ['Dave', 'John', 'Sara', 'Elsa', 'Jason']

# Extend the 'users' list by adding multiple new elements
users.extend(['Robert', 'Jimmy'])
print(users)  # Output: ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Insert 'Bob' at the beginning of the 'users' list
users.insert(0, 'Bob')
print(users)  # Output: ['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Insert 'Eddie' and 'Alex' starting at index 2
users[2:2] = ['Eddie', 'Alex']
print(users)  # Output: ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Replace elements at index 1 and 2 with 'Robert' and 'JPJ'
users[1:3] = ['Robert', 'JPJ']
print(users)  # Output: ['Bob', 'Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Remove the first occurrence of 'Bob' from the 'users' list
users.remove('Bob')
print(users)  # Output: ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# Remove and return the last element of the 'users' list
print(users.pop())  # Output: 'Jimmy'
print(users)  # Output: ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

# Delete the first element of the 'users' list
del users[0]
print(users)  # Output: ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

# Clear all elements from the 'data' list, leaving it empty
data.clear()
print(data)  # Output: []

# Replace the second element in 'users' with 'dave'
users[1:2] = ['dave']

# Sort the 'users' list in alphabetical order (case-sensitive)
users.sort()
print(users)  # Output: ['Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sara', 'dave']

# Sort the 'users' list in alphabetical order (case-insensitive)
users.sort(key=str.lower)
print(users)  # Output: ['dave', 'Elsa', 'Jason', 'JPJ', 'John', 'Robert', 'Sara']

# Initialize a list of numbers
nums = [4, 42, 78, 1, 5]

# Reverse the order of the elements in 'nums'
nums.reverse()
print(nums)  # Output: [5, 1, 78, 42, 4]

# Print a sorted (descending) version of 'nums' without modifying the original list
print(sorted(nums, reverse=True))  # Output: [78, 42, 5, 4, 1]

# Print the original 'nums' list to show it is unchanged
print(nums)  # Output: [5, 1, 78, 42, 4]

# Create a shallow copy of 'nums' using the .copy() method
numscopy = nums.copy()

# Create another shallow copy of 'nums' using the list() constructor
mynums = list(nums)

# Create another shallow copy of 'nums' using slicing
mycopy = nums[:]

# Print the different copies of the 'nums' list
print(numscopy)  # Output: [5, 1, 78, 42, 4]
print(mynums)    # Output: [5, 1, 78, 42, 4]

# Sort 'mycopy' in ascending order
mycopy.sort()
print(mycopy)  # Output: [1, 4, 5, 42, 78]

# Print the original 'nums' list to show it is unchanged
print(nums)  # Output: [5, 1, 78, 42, 4]

# Print the type of 'nums'
print(type(nums))  # Output: <class 'list'>

# Create a list with mixed data types using the list() constructor
mylist = list([1, "Neil", True])
print(mylist)  # Output: [1, 'Neil', True]
