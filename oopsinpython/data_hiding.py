# Define a function that hides a local variable
def hidden_function():
    __hidden_variable = "This is hidden"
    print("This is visible")


# Define a class that hides an attribute and a method
class HiddenClass:
    def __init__(self, name):
        self.name = name  # This is public
        self.__secret = "This is secret"  # This is private

    def public_method(self):
        print("This is public")

    def __private_method(self):
        print("This is private")


# Create an object of the class
obj = HiddenClass("Alice")

# Access the public attribute and method
print(obj.name)
obj.public_method()

# Try to access the private attribute and method
print(obj.__secret)  # This will raise an AttributeError
obj.__private_method()  # This will also raise an AttributeError

################################################################################################


# Define a class that hides the input variables and the addition method
class Adder:
    def __init__(self, a, b):
        self.__a = a  # This is private
        self.__b = b  # This is private

    def __add(self):
        return self.__a + self.__b  # This is private

    def show_result(self):
        print("The result is", self.__add())  # This is public


# Create an object of the class
obj = Adder(5, 7)

# Access the public method
obj.show_result()

# Try to access the private variables or method
print(obj.__a)  # This will raise an AttributeError
print(obj.__b)  # This will also raise an AttributeError
obj.__add()  # This will also raise an AttributeError
