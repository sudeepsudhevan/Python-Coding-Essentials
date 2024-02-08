# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Hierarchical Inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

print(dog.speak())
print(cat.speak())
print(cow.speak())