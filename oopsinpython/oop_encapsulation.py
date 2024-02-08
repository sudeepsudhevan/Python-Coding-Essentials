class Computer:
    def __init__(self) -> None:
        self.__maxprice = 900

    def setmaxprice(self, price):
        self.__maxprice = price


c = Computer()

c.__maxprice = 1000  # this will never work
c.setmaxprice(100)
print(c._Computer__maxprice)
