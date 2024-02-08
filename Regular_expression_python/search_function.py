import re

line = "The cats are smarter than dogs"

x = re.search("^The.smarter", line)

# print(x)

# if x:
#     print("YES!")
# else:
#     print("NO!")

y = re.search("^The.*dogs$", line)

if y:
    print("YES!")
else:
    print("NO!")
