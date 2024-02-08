# ZeroDivisionError

try:
    x = 10 / 0  # this will cause a ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!")

################################################################

# IndexError

try:
    lst = [1, 2, 3]
    print(lst[3])  # this will cause an IndexError
except IndexError:
    print("The index is out of range!")

##################################################################

# KeyError

try:
    dct = {"a": 1, "b": 2}
    print(dct["c"])  # this will cause a KeyError
except KeyError:
    print("The key does not exist!")

####################################################################

# NameError

try:
    print(foo)  # this will cause a NameError
except NameError:
    print("The name is not defined!")

##################################################################

# TypeError

try:
    print("Hello" + 1)  # this will cause a TypeError
except TypeError:
    print("You cannot add a string and an integer!")

#################################################################

# ValueError

try:
    int("abc")  # this will cause a ValueError
except ValueError:
    print("You cannot convert a string to an integer!")

#################################################################

# IOError

try:
    f = open("nonexistent.txt", "r")  # this will cause an IOError
except IOError:
    print("The file does not exist or cannot be opened!")
