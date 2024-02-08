# method overriding
class Parent:
    def myMethod(self):
        print("Calling method from parent class")
        print("hello world")


class Child(Parent):
    def myMethod(self):
        print("Calling method from child class")
        print("hello world!!!!!!!!!!!!")


c = Child()
c.myMethod()


# method overloading


# A class that demonstrates method overloading
class Calculator:
    # A method that adds two or more numbers and returns the result
    def add(self, *args):
        # Initialize the result to zero
        result = 0
        # Loop through the arguments and add them to the result
        for arg in args:
            result += arg
        # Return the result
        return result


# Creating an object of the class
calc = Calculator()

# Calling the add method with different arguments
print(calc.add(10, 20))  # prints 30
print(calc.add(10, 20, 30))  # prints 60
print(calc.add(10.5, 20.5))  # prints 31.0
