# What Are Decorators?
  * A decorator is a design pattern that wraps a function with another function.
  * The outer function (decorator) takes the original function as an argument and returns a modified version of it.
  * Essentially, decorators allow you to add functionality to functions dynamically.

1. **Creating a Decorator**

```
def ordinary():
    print("I am ordinary")
```
2. **create a decorator called `make_pretty()`:**

```
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()  # Call the original function
    return inner

decorated_func = make_pretty(ordinary)
decorated_func()  # Output: "I got decorated" followed by "I am ordinary"
```

In this example, `make_pretty()` wraps the `ordinary()` function, adding the “I got decorated” message before calling the original function.

3. **Using Decorators with the `@` Syntax**
 * Python provides a convenient syntax for applying decorators using the `@` symbol.
 * Here’s how you can use the `@` syntax to apply the `make_pretty()` decorator:

```
@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  # Output: "I got decorated" followed by "I am ordinary"
```

4. **Common Use Cases for Decorators:**
 * Logging: Add logging statements before and after function calls.
 * Authentication: Check user credentials before executing a function.
 * Measuring Execution Time: Record how long a function takes to run.
 * Caching: Store function results to avoid recomputation.
 * Validation: Validate input arguments before invoking a function.

5. **Chaining Decorators:**
 * You can apply multiple decorators to a single function.
 * The order matters: the innermost decorator is applied first.
 Example:

```
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclamation(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@exclamation
@uppercase
def greet():
    return "hello"

print(greet())  # Output: "HELLO!"
```   
