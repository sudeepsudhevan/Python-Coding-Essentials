class Shape:
    def __init__(self) -> None:
        self.color = (0, 0, 0)


class Rectangle(Shape):
    def __init__(self, w, h):
        Shape.__init__(self)  # or super().__init__()
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height


r1 = Rectangle(10, 5)

print(r1.area())

print(r1.color)
