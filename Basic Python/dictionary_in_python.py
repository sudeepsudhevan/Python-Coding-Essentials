# Creating a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Accessing elements of a dictionary
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Modifying a dictionary
my_dict["age"] = 26
print("Modified Dictionary:", my_dict)

# Adding a new key-value pair to a dictionary
my_dict["occupation"] = "Engineer"
print("Dictionary with new key-value pair:", my_dict)

# Removing a key-value pair from a dictionary
removed_value = my_dict.pop("city")
print("Removed value:", removed_value)
print("Dictionary after removing 'city':", my_dict)

# Checking if a key is present in a dictionary
key_to_check = "name"
if key_to_check in my_dict:
    print(f"'{key_to_check}' is present in the dictionary")
else:
    print(f"'{key_to_check}' is not present in the dictionary")

# Getting all keys and values from a dictionary
all_keys = my_dict.keys()
all_values = my_dict.values()
print("All keys:", all_keys)
print("All values:", all_values)

# Getting key-value pairs as tuples
key_value_pairs = my_dict.items()
print("Key-Value pairs:", key_value_pairs)

# Clearing all items in a dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)
