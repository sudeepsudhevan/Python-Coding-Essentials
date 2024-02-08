#OOPS in Python

1. Python Classes and Objects:
   
A class is a blueprint or prototype for creating objects. It defines attributes (variables) and methods (functions) that the objects of that class will have.
An object is an instance of a class. It has its own state (attributes) and behavior (methods).
Example of creating a simple class and objects:

```
class Dog:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

dog1 = Dog(breed="Golden Retriever", age=3)
dog2 = Dog(breed="Labrador", age=2)

print(f"{dog1.breed} is {dog1.age} years old")
print(f"{dog2.breed} is {dog2.age} years old")

Output:
Golden Retriever is 3 years old
Labrador is 2 years old
```

2. Inheritance:
Inheritance allows you to create a new class (derived class) based on an existing class (base class). The derived class inherits attributes and methods from the base class.
Example of using inheritance:

```
class Animal:
    def eat(self):
        print("I can eat!")

class Dog(Animal):
    def bark(self):
        print("I can bark! Woof woof!!")

dog1 = Dog()
dog1.eat()
dog1.bark()

Output:
I can eat!
I can bark! Woof woof!!
```

3. Encapsulation:
Encapsulation bundles data (attributes) and methods (functions) together within a class. It prevents direct access to internal attributes and promotes data hiding.
Example of encapsulation:

```
class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()  # Output: Selling Price: 900
c.setMaxPrice(1000)
c.sell()  # Output: Selling Price: 1000
```
