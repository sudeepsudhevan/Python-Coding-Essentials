# Lambda Functions Sample

1. Basic lambda functions
  A lambda function is defined using the lambda keyword, followed by the arguments and an expression. Here’s a simple example that prints “Hello World”:

```
greet = lambda: print('Hello World')
greet()  # Output: Hello World
```

2. Lambda Function with an Argument
   create lambda functions that accept arguments. For instance, this lambda function takes a name and greets the user

```
greet_user = lambda name: print(f'Hey there, {name}')
greet_user('Delilah')  # Output: Hey there, Delilah
```
   
3. Using Lambda with map()
   The map() function applies a given function to each item in an iterable. Here’s an example that squares each number in a list

```
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```
   
4. Using Lambda with filter()
   The filter() function filters elements based on a given condition. In this example, we filter out even numbers from a list

```
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print(even_numbers)  # Output: [4, 6, 8, 12]
```
   
5. Power Functions
   You can even return a lambda function from another function. Here’s an example that defines functions for squaring, cubing, and finding square roots

```
import math

def power_function(n):
    return lambda a: math.pow(a, n)

square = power_function(2)
cube = power_function(3)
squareroot = power_function(0.5)

print(square(3))  # Output: 9.0
print(cube(3))    # Output: 27.0
print(squareroot(3))  # Output: 1.7320508075688772
```   
      
