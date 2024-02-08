# Python-Problems

* Print Hello World in python

syntax of print : 
  print(object(s), sep=separator, end=end, file=file, flush=flush)

```
print('Hello World')
```

* Python BMI Calculator

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

* Enter a number. Find it odd or even

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




