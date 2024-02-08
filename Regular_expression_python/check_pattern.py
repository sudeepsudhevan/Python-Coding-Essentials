import re

line = "The cats are smaller than dogs"  # it has 6 words

# x = re.search(r"\bdogs", line) # return match if specified character are at begining or end of a word

# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

############################################################

# x = re.search(
#     r"\Bats", line
# )  # return match if specified character NOT at beginning or end of a word

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

############################################################

# x = re.search(r"\s", line)
# #  return match if there is a space
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

############################################################

# x = re.search(r"\S", line)
# #  return match if there is a string which is not a space
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

############################################################

# x = re.search(r"\w", line)
# #  return match if there is a word
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

#############################################################

# x = re.search(r"\W", line)
# #  return match if there is NOT a word at any point of the string
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

#############################################################

x = re.search(r"dogs\Z", line)
#  return match if specified character are at end of a word
print(x)

if x:
    print("YES! it is a match")
else:
    print("NO! it is not a match")
