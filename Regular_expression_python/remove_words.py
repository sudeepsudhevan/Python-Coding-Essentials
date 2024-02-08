# Python program to remove words from a string of length between 1 and a given number

import re

text = "Clearly, he has no excuse for such behavior."

# shortword = re.compile(r"\W*\b\w{1,3}\b")

# \W is a special character which matches any non-word character
# \b matches the word boundary
# \w{1,3} matches any word character between 1 and 3

# print(shortword)

# print(shortword.sub("", text))

line = "Indian independence"

shortword = re.compile("pen")

result = shortword.sub("", line)

print(result)
