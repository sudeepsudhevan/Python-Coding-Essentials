# Python-Problems

1. **Print Hello World in python**

syntax of print : 
  print(object(s), sep=separator, end=end, file=file, flush=flush)

```
print('Hello World')
```

2. **Swap Two numbers**

```
num1 = int(input('Enter the First Number: '))
num2 = int(input('Enter the Second Number: '))

print(f'Initially num1 is {num1}')
print(f'Initially num2 is {num2}')

swap = num1
num1 = num2
num2 = swap

print(f'\nNow num1 is {num1}')
print(f'Now num2 is {num2}')
```

3. **Python BMI Calculator**

```
# BMI Calculator in Python

# Receive input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# Convert height to meters
height_meters = height / 100

# Calculate the BMI
bmi = weight / (height_meters * height_meters)

# Display the result to the user
print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
```

4. **Input a number. Find it odd or even**

```
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))

if (num % 2) == 0:
    print("{0} is **Even**.".format(num))
else:
    print("{0} is **Odd**.".format(num))
```

5. **Python program to check if a year is a leap year or not**

  * A year is a leap year if it is divisible by 4, except for century years (years ending with 00).
  * A century year is a leap year only if it is perfectly divisible by 400.

```
# To get the year (integer input) from the user:
year = int(input("Enter a year: "))
# Check if it's a century year (ending with 00)
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
# Check if it's not a century year
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")
# If not divisible by both 400 (century year) and 4 (not century year)
else:
    print(f"{year} is not a leap year")
```

6. **FizzBuzz**
  
The task is to write a program that prints the numbers from 1 to 100, but for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

```
# FizzBuzz in Python
for i in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # check if the number is divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0: # check if the number is divisible by 3
        print("Fizz")
    elif i % 5 == 0: # check if the number is divisible by 5
        print("Buzz")
    else: # otherwise, just print the number
        print(i)
```

7. **Prime Numbers**

```
# Program to check if a number is prime or not
num = 29  # You can change this value to check other integers

# Define a flag variable
flag = False

if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    # Check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # If a factor is found, set flag to True and break out of the loop
            flag = True
            break

    # Check if flag is True
    if flag:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

```

