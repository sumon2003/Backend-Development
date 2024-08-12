# Dictionaries

# Define a dictionary representing a band with vocals and guitar roles
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# Define another dictionary using the dict() constructor with the same key-value pairs
band2 = dict(vocals="Plant", guitar="Page")

# Print both dictionaries to show their content
print("band:", band)
print("band2:", band2)

# Print the type of 'band', which will be <class 'dict'>
print("Type of 'band':", type(band))

# Print the number of items in 'band'
print("Number of items in 'band':", len(band))

# Access items in the dictionary
print("Vocals:", band["vocals"])          # Access value using key
print("Guitar:", band.get("guitar"))      # Access value using the get() method

# List all keys in the dictionary
print("Keys in 'band':", band.keys())

# List all values in the dictionary
print("Values in 'band':", band.values())

# List all key-value pairs as tuples
print("Items in 'band':", band.items())

# Verify if certain keys exist in the dictionary
print("'guitar' in band:", "guitar" in band)  # True, key exists
print("'triangle' in band:", "triangle" in band)  # False, key does not exist

# Change values in the dictionary
band["vocals"] = "Coverdale"  # Update existing key
band.update({"bass": "JPJ"})  # Add new key-value pair

# Print the updated dictionary
print("Updated 'band':", band)

# Remove items from the dictionary
print("Removed item:", band.pop("bass"))  # Remove and return value of key 'bass'
print("After pop:", band)

# Add a new item to the dictionary
band["drums"] = "Bonham"
print("After adding 'drums':", band)

# Remove the last item added (popitem() returns a tuple of key-value pair)
print("Removed item:", band.popitem())  # Output: tuple (key-value pair)
print("After popitem:", band)

# Delete a specific key-value pair
band["drums"] = "Bonham"
del band["drums"]
print("After deleting 'drums':", band)

# Clear all items from 'band2'
band2.clear()
print("After clearing 'band2':", band2)

# Delete the dictionary 'band2'
del band2
# print(band2)  # This would raise an error because 'band2' no longer exists

# Copy dictionaries

# The following code creates a reference, not a copy (commented out to avoid overwriting)
# band2 = band
# print("Bad copy!")
# print("band2:", band2)
# print("band:", band)

# Modify the copy to demonstrate that it affects the original
# band2["drums"] = "Dave"
# print("Modified band:", band)

# Create a proper copy of 'band' into 'band2'
band2 = band.copy()
band2["drums"] = "Dave"  # Modify the copy
print("Good copy!")
print("Original 'band':", band)
print("Copied 'band2':", band2)

# Another way to copy a dictionary using the dict() constructor
band3 = dict(band)
print("Another good copy!")
print("Copied 'band3':", band3)

# Nested dictionaries

# Define nested dictionaries for band members
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

# Print the nested dictionary
print("Nested 'band':", band)

# Access a nested value
print("Name of 'member1':", band["member1"]["name"])
