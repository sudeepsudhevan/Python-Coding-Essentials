import re

line = "The cats are smaller than dogs"  # it has 6 words

# x = re.findall(
#     r"[atn]", line
# )  # return a match of only all matching characters.

# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

############################################################

# x = re.findall(r"[a-n]", line)  # return a match for any lower case character between a and n

# x = re.findall(r"[^arn]", line) # return match except arn

# [a-z] - return a match for any lower case character between a and z
# [0-9] - return a match for any digit between 0 and 9
# [a-zA-Z] - return a match for any lower case character or any upper case character
# [0-5][0-9] - return a match for any two digits between 00 and 59
