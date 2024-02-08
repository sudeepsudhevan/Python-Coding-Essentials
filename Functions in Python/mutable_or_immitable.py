# Mutable objects, such as lists, dictionaries, and sets, can be changed inside the function and the changes
# will be reflected outside the function as well. This is similar to call by reference in some other languages.
# Immutable objects, such as numbers, strings, and tuples, cannot be changed inside the function and the changes
#  will not affect the original object outside the function. This is similar to call by value in some other languages

###########################################################################################################


# Example of call by value with an immutable object (number)
def add_one(num):
    num = num + 1  # This creates a new object with a different value
    print("Inside the function:", num)


x = 10  # x is assigned to the object 10
add_one(x)  # The function receives a reference to the same object 10
print("Outside the function:", x)  # x is still assigned to the same object 10

# Output:
# Inside the function: 11
# Outside the function: 10


# Example of call by reference with a mutable object (list)
def append_zero(lst):
    lst.append(0)  # This modifies the same object that lst refers to
    print("Inside the function:", lst)


y = [1, 2, 3]  # y is assigned to a list object
append_zero(y)  # The function receives a reference to the same list object
print(
    "Outside the function:", y
)  # y is still assigned to the same list object, which has been modified

# Output:
# Inside the function: [1, 2, 3, 0]
# Outside the function: [1, 2, 3, 0]
