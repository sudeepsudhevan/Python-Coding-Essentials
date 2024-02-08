# Python Functions Problems

1. **Write a Python function that takes three numbers as input and returns the maximum among them**

```
def find_maximum(a, b, c):
    return max(a, b, c)

result = find_maximum(5, 12, 8)
print(f"The maximum value is: {result}")

```

2. **Write a Python function that accepts a list of numbers and returns their sum.**

```
def sum_of_list(numbers):
    return sum(numbers)

sample_list = [8, 2, 3, 0, 7]
total_sum = sum_of_list(sample_list)
print(f"The sum of the list is: {total_sum}")

```

3. **Create a Python function that multiplies all the numbers in a given list.**

```
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

sample_list = [8, 2, 3, -1, 7]
product = multiply_list(sample_list)
print(f"The product of the list is: {product}")

```

4. **Write a Python program to reverse a given string.**

```
def reverse_string(input_string):
    return input_string[::-1]

sample_string = "1234abcd"
reversed_string = reverse_string(sample_string)
print(f"The reversed string is: {reversed_string}")

```

5. **Create a Python function that calculates the factorial of a non-negative integer. The factorial of n is denoted as n! and is the product of all positive integers from 1 to n.**

```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
factorial_result = factorial(num)
print(f"The factorial of {num} is: {factorial_result}")

```

6. **More Sample Code snippets**
   * [Blind Auction](https://gist.github.com/sudeepsudhevan/362a431bcfe392848b754ff0fc833b81)
   * [Travel log](https://gist.github.com/sudeepsudhevan/60f0ff5fc27529cd9499995c27e67852)
   * [Prime number or not](https://gist.github.com/sudeepsudhevan/897f7c63c3ccbf4bb088b17e2d20e131)
