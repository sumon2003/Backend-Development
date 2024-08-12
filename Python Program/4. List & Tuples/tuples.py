# Working with Tuples

# Create a tuple named 'mytuple' using the tuple() constructor.
# The tuple contains three elements: a string ('Dave'), an integer (42), and a boolean (True).
mytuple = tuple(('Dave', 42, True))

# Create another tuple named 'anothertuple' with six integer elements.
anothertuple = (1, 4, 2, 8, 2, 2)

# Print the contents of 'mytuple'.
print(mytuple)  # Output: ('Dave', 42, True)

# Print the type of 'mytuple'.
print(type(mytuple))  # Output: <class 'tuple'>

# Print the type of 'anothertuple'.
print(type(anothertuple))  # Output: <class 'tuple'>

# Convert 'mytuple' into a list and store it in 'newlist'.
# This allows for mutable operations like appending.
newlist = list(mytuple)

# Append the string 'Neil' to 'newlist'.
newlist.append('Neil')

# Convert 'newlist' back into a tuple and store it in 'newtuple'.
newtuple = tuple(newlist)

# Print the contents of 'newtuple'.
print(newtuple)  # Output: ('Dave', 42, True, 'Neil')

# Unpack 'anothertuple' into variables:
# - 'one' gets the first element (1)
# - 'hey' gets the last element (2)
# - The middle elements [4, 2, 8, 2] are collected into 'two'
(one, *two, hey) = anothertuple

# Print the value of 'one'.
print(one)  # Output: 1

# Print the list 'two', containing the middle elements.
print(two)  # Output: [4, 2, 8, 2]

# Print the value of 'hey'.
print(hey)  # Output: 2

# Count how many times the integer 2 appears in 'anothertuple' and print the result.
print(anothertuple.count(2))  # Output: 3
