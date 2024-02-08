# A string is a sequence of characters enclosed in quotes
s = "Hello, world!"

# String operations include concatenation (+), repetition (*), indexing ([]), and slicing ([:])
print(s + " This is a string operation.")  # Concatenation
print(s * 2)  # Repetition
print(s[0])  # Indexing
print(s[1:5])  # Slicing

# String functions are built-in functions that can be applied to strings
print(len(s))  # len() returns the length of a string
print(str(42))  # str() converts a value to a string
print(chr(65))  # chr() returns the character corresponding to an ASCII code
print(ord("A"))  # ord() returns the ASCII code of a character

# String methods are functions that are defined for string objects
print(s.upper())  # upper() returns a copy of the string in uppercase
print(s.lower())  # lower() returns a copy of the string in lowercase
print(
    s.replace("world", "Python")
)  # replace() returns a copy of the string with some substrings replaced
print(s.split(","))  # split() returns a list of substrings separated by a delimiter
