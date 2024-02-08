# polymorphism sample


class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# Here we have two classes: Parrot and Penguin. Both of them have a method called fly(),
# but they have different implementations


def fly_test(bird):
    bird.fly()


# This function calls the fly() method of the bird object. This is an example of polymorphism,
# because the fly_test() function can work with any object that has a fly() method, regardless of its class.

blue = Parrot()
peg = Penguin()

fly_test(blue)
fly_test(peg)
