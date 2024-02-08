import re

split_string = "Python Programming Language"

# result = re.split(r"i", split_string)

# print(result)

# result = re.split(r"n", split_string)

# print(result)

result = re.split(r"n", split_string, maxsplit=1)
print(result)
