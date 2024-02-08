def enter_age(num):
    if num < 0:
        raise ValueError("Only positive number is allowed")
    if num % 2 == 0:
        print("num is even")
    else:
        print("num is odd")


num = int(input("Enter any number: "))
enter_age(num)

# try:
#     num = int(input("Enter any number: "))
#     enter_age(num)
# except ValueError:
#     print("Only postive number")
# except:
#     print("something is wrong")
