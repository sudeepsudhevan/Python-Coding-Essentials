import re

email = input("Enter an email Address: ")
# email = "sudeepsudhevan@gmail.com"

pattern = r"(\w+)@(\w+)\.(com)"

result = re.match(pattern, email)

print(result.group(1))

print(result.group(2))
