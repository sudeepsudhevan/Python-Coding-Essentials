import re

patterns = ["this", "that"]

text = "Does this text have a match?"

for pattern in patterns:
    print(f'Searching for "{pattern}"')
    if re.search(pattern, text):
        print("Match found")
    else:
        print("No match")
