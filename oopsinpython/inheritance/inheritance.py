# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "i don't speak"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Multiple Inheritance
class Flyable:
    def fly(self):
        return f"{self.name} can fly."

class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} says Chirp!"

# Multilevel Inheritance
class Reptile(Animal):
    def crawl(self):
        return f"{self.name} can crawl."

class Snake(Reptile):
    def hiss(self):
        return f"{self.name} says Hiss!"

# Single Inheritance
dog = Dog("Buddy")
print(dog.speak())

# Multiple Inheritance
bird = Bird("Robin")
print(bird.speak())
print(bird.fly())

# Multilevel Inheritance
snake = Snake("Python")
print(snake.speak())
print(snake.crawl())
print(snake.hiss())