# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to a set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing an element from a set
my_set.remove(5)
print("Set after removing 5:", my_set)

# Checking if an element is present in a set
element_to_check = 4
if element_to_check in my_set:
    print(f"{element_to_check} is present in the set")
else:
    print(f"{element_to_check} is not present in the set")

# Finding the length of a set
set_length = len(my_set)
print("Length of the set:", set_length)

# Converting a set to a list
set_list = list(my_set)
print("Set converted to a list:", set_list)

# Creating another set
another_set = {3, 4, 5, 6, 7}

# Performing set operations
union_set = my_set.union(
    another_set
)  # union() returns a new set containing all the elements from both sets
print("Union of the sets:", union_set)

intersection_set = my_set.intersection(
    another_set
)  # intersection() returns a new set containing only the common elements from both sets
print("Intersection of the sets:", intersection_set)

difference_set = my_set.difference(
    another_set
)  # difference() returns a new set containing only the elements from the first set that are not in the second set
print("Difference of the sets:", difference_set)

symmetric_difference_set = my_set.symmetric_difference(
    another_set
)  # symmetric_difference() returns a new set containing only the elements that are not common in both sets
print("Symmetric difference of the sets:", symmetric_difference_set)
