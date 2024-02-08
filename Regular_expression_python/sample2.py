import re

regex = r"([a-zA-Z]+) ?(\d+)"

if re.search(regex, "June 24"):
    match = re.search(regex, "June 24")
    # print(match)
    print("Match at index %s, %s" % (match.start(), match.end()))

    print("Full match: %s" % match.group(2))
