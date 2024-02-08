# What Are Decorators?
  * A decorator is a design pattern that wraps a function with another function.
  * The outer function (decorator) takes the original function as an argument and returns a modified version of it.
  * Essentially, decorators allow you to add functionality to functions dynamically.

Creating a Decorator

```
def ordinary():
    print("I am ordinary")
```
create a decorator called make_pretty():
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()  # Call the original function
    return inner

decorated_func = make_pretty(ordinary)
decorated_func()  # Output: "I got decorated" followed by "I am ordinary"

In this example, make_pretty() wraps the ordinary() function, adding the “I got decorated” message before calling the original function.
