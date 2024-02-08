import re

text = "2That will be 59 dollars"

# x = re.findall("\d", text)

# # print(x)

# y = re.findall("w..l", text)

# print(y)

###################################################

# x = re.search("[0-9]\d", text)

# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

###################################################

x = re.search(r"\D", text)  # return match if there is a string which is not a digit

print(x)

if x:
    print("YES! it is a match")
else:
    print("NO! it is not a match")
