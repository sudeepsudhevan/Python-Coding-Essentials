import re

# print(re.sub("ub", "~*", "Subject has Uber booked already", flags=re.IGNORECASE))

# print(re.sub("ub", "~*", "Subject has Uber booked already"))

# print(re.sub("ub", "~*", "Subject has Uber booked already", count=1, flags=re.I))

print(re.sub(r"\sAND\s", " & ", "Baked Beans And Spam", flags=re.IGNORECASE))
