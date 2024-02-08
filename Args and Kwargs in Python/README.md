# ARGS AND KWARGS in Python

1. `*args` (Non-Keyword Arguments):
    * When you’re unsure about the number of arguments to pass to a function, you can use `*args`.
    * It allows you to pass a variable number of non-keyword arguments to a function.
    * Inside the function, the arguments are treated as a tuple.
    * Example using `*args`:

```
def adder(*num):
    total_sum = sum(num)
    print(f"Sum: {total_sum}")

adder(3, 5)          # Output: Sum: 8
adder(4, 5, 6, 7)    # Output: Sum: 22
adder(1, 2, 3, 5, 6) # Output: Sum: 17

```

2. `**kwargs` (Keyword Arguments):
    * While *args handles non-keyword arguments, `**kwargs` deals with keyword arguments.
    * It allows you to pass a variable number of keyword arguments (as a dictionary) to a function.
    * Example using `**kwargs`:

```
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="Wonderland")
# Output:
# name: Alice
# age: 30
# city: Wonderland

```

3. Combining `*args` and `**kwargs`:

```
def example_function(*args, **kwargs):
    for arg in args:
        print(f"Non-keyword argument: {arg}")
    for key, value in kwargs.items():
        print(f"Keyword argument: {key} = {value}")

example_function(1, 2, 3, name="Bob", age=25)
# Output:
# Non-keyword argument: 1
# Non-keyword argument: 2
# Non-keyword argument: 3
# Keyword argument: name = Bob
# Keyword argument: age = 25

```
   
      
