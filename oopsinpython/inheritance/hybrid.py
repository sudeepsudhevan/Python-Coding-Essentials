class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Flyable:
    def fly(self):
        return f"{self.name} can fly."

class Swimmable:
    def swim(self):
        return f"{self.name} can swim."

# Hybrid Inheritance
class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} says Chirp!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} says Quack!"

# Hybrid Inheritance
bird = Bird("Robin")
print(bird.speak())
print(bird.fly())

duck = Duck("Donald")
print(duck.speak())
print(duck.fly())
print(duck.swim())