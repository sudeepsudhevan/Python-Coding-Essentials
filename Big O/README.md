## 1. Big O: O(n) 
Linear Time
* Directly proportional to the data set size.
* Example: Looping through an array.

```py
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)
```

## 2. Big O: O(n<sup>2</sup>)
Polynomial Time
* Nested loops for each power of n.
* Example: Bubble sort (O(n2)), Nested loop.

```py
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)
```

## 4. Big O: O(1)
Constant Time
* Doesn't depend on the size of the data set.
* Example: Accessing an array element by its index.

```py
def add_two_number(n):
    return n + n

add_two_number(10)
```

## 5. Big O: O(logn)
Logarithmic Time
* Splits the data in each step (divide and conquer).
* Example: Binary search.

```py

```

## 6. Big O: O(nlogn)
Linearithmic Time
* Splits and sorts or searches data.
* Example: Merge sort, quick sort.

```py

```


