# List Comprehensions:

syntax:

`new_list = [expression for item in iterable if condition]`

Example

```
# Create a list of squares for numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

# Dictionary Comprehensions:

syntax:

`new_dict = {key: value for key, value in iterable if condition}`

Example

```
# Create a dictionary from a list of tuples (name, age)
data = [('Alice', 30), ('Bob', 25), ('Charlie', 22)]
name_to_age = {name: age for name, age in data}
print(name_to_age)
# Output: {'Alice': 30, 'Bob': 25, 'Charlie': 22}
```

Also can use conditions in dictionary comprehensions:
```
# Create a dictionary with only ages greater than 25
adults = {name: age for name, age in name_to_age.items() if age > 25}
print(adults)
# Output: {'Alice': 30}
```

Sample code

  * [Celsius to fahrenheit](https://gist.github.com/sudeepsudhevan/08d258b1e9f52ca214009a518c3e6761)
