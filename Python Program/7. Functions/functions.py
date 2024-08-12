# Function to print "Hello world!"
def hello_world():
    print("Hello world!")

# Call the function to execute it
hello_world()  # Output: Hello world!

# Function to sum two numbers with default values
def sum(num1=0, num2=0):
    # Check if both num1 and num2 are integers
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return 0  # Return 0 if either value is not an integer
    return num1 + num2  # Return the sum of num1 and num2

# Call the sum function with arguments 7 and 2
total = sum(7, 2)
print(total)  # Output: 9

# Function to handle a variable number of positional arguments
def multiple_items(*args):
    # Print the tuple of arguments
    print(args)  # Output: ('Dave', 'John', 'Sara')
    # Print the type of args, which is a tuple
    print(type(args))  # Output: <class 'tuple'>

# Call the function with three positional arguments
multiple_items("Dave", "John", "Sara")

# Function to handle a variable number of keyword arguments
def mult_named_items(**kwargs):
    # Print the dictionary of keyword arguments
    print(kwargs)  # Output: {'first': 'Dave', 'last': 'Gray'}
    # Print the type of kwargs, which is a dictionary
    print(type(kwargs))  # Output: <class 'dict'>

# Call the function with two keyword arguments
mult_named_items(first="Dave", last="Gray")
