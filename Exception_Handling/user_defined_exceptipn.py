class ValueTooSmallError(OSError):
    """Raised when the input value is too small"""

    pass


class ValueTooLargeError(OSError):
    """Raised when the input value is too large"""

    pass


import random

number = random.randint(1, 20)

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")
print("Congratulations! You guessed it correctly.")
