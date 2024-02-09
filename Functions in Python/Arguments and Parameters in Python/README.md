# Arguments and Parameter

1. Parameters:
  * A parameter is a variable defined within the parentheses during function definition.
  * Parameters are written when we declare a function.
  * They act as placeholders for values that will be passed to the function when it is called.
  * For example:
```
def sum(a, b):
    print(a + b)

# 'a' and 'b' are parameters

```

2. Arguments:
  * An argument is a value that is passed to a function when it is called.
  * It can be a variable, a literal value, or an object.
  * Arguments are written when we actually call the function.
  * For example:
```
def sum(a, b):
    print(a + b)

# 1 and 2 are arguments
sum(1, 2)  # Output: 3

```

## Different Types of Arguments

1. **Positional Arguments:**
 * These are the most common type of arguments. They are passed in the order defined by the function parameters.
```
def add_numbers(a, b):
    sum_result = a + b
    print("Sum:", sum_result)

add_numbers(2, 3)  # Output: Sum: 5
```

2. **Default Value Arguments:**
 * You can provide default values for function parameters. If an argument is not explicitly passed, the default value is used.
```
def add_numbers(a=7, b=8):
    sum_result = a + b
    print("Sum:", sum_result)

add_numbers(2)  # Output: Sum: 10
add_numbers()   # Output: Sum: 15
```

3. **Keyword Arguments:**
 * Arguments are assigned based on their names, regardless of their order.
```
def display_info(first_name, last_name):
    print("First Name:", first_name)
    print("Last Name:", last_name)

display_info(last_name="Cartman", first_name="Eric")
# Output: First Name: Eric, Last Name: Cartman
```

4. **Arbitrary Arguments (Variable-Length Arguments) `*args`:**
 * Use an asterisk (`*`) before the parameter name to handle a varying number of arguments.
```
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    print("Sum =", result)

find_sum(1, 2, 3)  # Output: Sum = 6
find_sum(4, 9)     # Output: Sum = 13
```

5. **Arbitrary Arguments (Keyword Arguments) `**kwargs`:**
   * **kwargs accepts keyword (or named) arguments.
```
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(first='Geeks', second='for', third='Geeks')
# Output:
# first: Geeks
# second: for
# third: Geeks
```
