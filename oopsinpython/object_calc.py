class calculation:
    def __init__(self, num1, num2) -> None:
        self.a = num1
        self.b = num2

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


calc = calculation(12, 6)

print(calc.div())
