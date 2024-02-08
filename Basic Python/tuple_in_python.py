# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print("Tuple elements:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
subset_tuple = my_tuple[1:4]
print("Subset of the tuple:", subset_tuple)

# Finding the length of a tuple
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)

# Checking if an element is present in a tuple
element_to_check = 3
if element_to_check in my_tuple:
    print(f"{element_to_check} is present in the tuple")
else:
    print(f"{element_to_check} is not present in the tuple")

# Counting occurrences of an element in a tuple
element_count = my_tuple.count(3)
print(f"Number of occurrences of 3 in the tuple: {element_count}")

# Finding the index of an element in a tuple
element_index = my_tuple.index(4)
print(f"Index of 4 in the tuple: {element_index}")

# Converting a tuple to a list
tuple_list = list(my_tuple)
print("Tuple converted to a list:", tuple_list)

# Concatenating tuples
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", new_tuple)
