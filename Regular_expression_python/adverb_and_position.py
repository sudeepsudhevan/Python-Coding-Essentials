import re

text = "Clearly, he has no excuse for his behavior."

for m in re.finditer(r"\w+ly", text):
    print(m.start(), m.end(), m.group(0))

text = "Finally, he failed."

for m in re.finditer(r"\w+ly", text):
    print(m.start(), m.end(), m.group(0))
