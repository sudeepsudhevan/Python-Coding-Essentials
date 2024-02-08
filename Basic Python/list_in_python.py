# A list is a sequence of values enclosed in brackets
my_list = [1, 2, 3, 4, 5]

# Accessing elements of a list
print("List elements:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing a list
subset_list = my_list[1:4]
print("Subset of the list:", subset_list)

# Finding the length of a list
list_length = len(my_list)
print("Length of the list:", list_length)

# Checking if an element is present in a list
element_to_check = 3
if element_to_check in my_list:
    print(f"{element_to_check} is present in the list")
else:
    print(f"{element_to_check} is not present in the list")

# Counting occurrences of an element in a list
element_count = my_list.count(3)
print(f"Number of occurrences of 3 in the list: {element_count}")

# Finding the index of an element in a list
element_index = my_list.index(4)
print(f"Index of 4 in the list: {element_index}")

# Converting a list to a tuple
list_tuple = tuple(my_list)
print("List converted to a tuple:", list_tuple)

# Concatenating lists
new_list = my_list + [6, 7, 8]
print("Concatenated list:", new_list)
