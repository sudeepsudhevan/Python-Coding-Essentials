class Human:
    def __init__(self, name, height, weight) -> None:
        self.name = name
        self.height = height
        self.weight = weight

    def eating(self, fruit):
        return f"{self.name} is eating {fruit}"


ram = Human("Ram", 6, 60)

ravi = Human("ravi", 5.9, 56)

print(f"Height of {ram.name} is {ram.height} and Weight is {ram.weight}")

print(ram.eating("Pine Apple"))

print(f"Height of {ravi.name} is {ravi.height} and Weight is {ravi.weight}")

print(ravi.eating("Pine Apple"))
