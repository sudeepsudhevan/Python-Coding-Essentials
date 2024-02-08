# function without argument and no return

a = 10
b = 20


def add():
    sum = a + b
    print("result is", sum)


add()


# function with argument and no return
def add(a, b):
    m = a + b
    print("result is", m)


add(12, 13)

# function without argument and return

a = 10
b = 20


def add():
    sum = a + b
    print("result is", sum)


add()

# function with argument and return


def add(a, b):
    sum = a + b
    return sum


result = add(20, 30)
print("result is", result)
