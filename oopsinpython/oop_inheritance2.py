class Parent:
    parentAttr = 100

    def __init__(self) -> None:
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling method from parent class")

    def write_number(self, attr):
        Parent.parentAttr = attr

    def read_number(self):
        print("Parent Attribute: ", Parent.parentAttr)


class Child(Parent):
    def __init__(self) -> None:
        # super().__init__()
        print("From the child constructor")

    def childMethod(self):
        print("Calling method from child Class")


c = Child()

c.childMethod()
c.parentMethod()
c.write_number(200)
c.read_number()
