try:
    num1, num2 = input("Enter two numbers, seperated by comma: ").split(",")
    print(num1, num2)
    result = int(num1) / int(num2)
    print(result)
except ZeroDivisionError:
    print("Division by zero error")
except:
    print("wrong input")
