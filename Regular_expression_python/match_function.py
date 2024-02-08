import re

pattern = r"Python"
sequence = "Python"

seq = "Pyton"

# if re.match(pattern, sequence):
#     print("Match")
# else:
#     print("Not Match")

if re.match(pattern, seq):
    print("Match")
else:
    print("Not Match")
