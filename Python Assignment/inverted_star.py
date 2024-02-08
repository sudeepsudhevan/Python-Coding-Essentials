# Print an inverted Star pattern

rows = int(input("Enter the no.of rows: "))

for a in range(0, rows + 1, 1):
    for b in range(a):
        print("*", end=" ")
    print()

# Enter the no.of rows: 4

# *
# * *
# * * *
# * * * *


for a in range(rows, 0, -1):
    for b in range(a):
        print("*", end=" ")
    print()

# Enter the no.of rows: 4
# * * * *
# * * *
# * *
# *
