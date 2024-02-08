import re

string = "hello 12 132 001 hi 89. Howdy 34"

pattern = "\d+"

result = re.findall(pattern, string)

print(result)
