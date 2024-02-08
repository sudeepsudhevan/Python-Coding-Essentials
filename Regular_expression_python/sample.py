import re

text = "The quick brown fox jumps over the lazy dog"

x = re.findall("[a-c]", text)

print(x)
