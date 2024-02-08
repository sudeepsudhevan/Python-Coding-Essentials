import re

line = "The cats are smaller than dogs"  # it has 6 words

# x = re.search(r"[a-z]", line)
# # return match if there is a lower case letter
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

#################################################################
# line = "python"

# x = re.search(r"s..l", line)
# # return match if there is character (. is any character)
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

# # output -
# # <re.Match object; span=(13, 17), match='smal'>
# # YES! it is a match

######################################################################

# x = re.search("^The", line)
# # return match if there is match at beginning
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

######################################################################

# x = re.search("dogs$", line)
# # return match if there is match at end
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

########################################################################

# x = re.search("sm.*r", line)
#
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

# # <re.Match object; span=(13, 20), match='smaller'>

########################################################################

# x = re.search("sm.+r", line)
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

#########################################################################

# x = re.search("sm.{4}r", line)  # exact character in between is 4
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

# # <re.Match object; span=(13, 20), match='smaller'>

###########################################################################

# x = re.search("smalle.?r", line)  # return if 0 or 1 character in between
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

###########################################################################

# x = re.search("cats|dogs", line)  # if there is match either cats or dogs
# print(x)

# if x:
#     print("YES! it is a match")
# else:
#     print("NO! it is not a match")

###########################################################################
