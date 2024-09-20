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

## 5. Big O: O(log n)
Logarithmic Time
* Splits the data in each step (divide and conquer).
* Example: Binary search.

```py
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage
array = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(array, target)
print("Element found at index:", result)

```


## 6. Big O: O(n log n)
Linearithmic Time
* Splits and sorts or searches data.
* Example: Merge sort, quick sort.

```py
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array)
print("Sorted array is:", array)

```

![Big O](https://github.com/user-attachments/assets/782ae9cc-423f-4d50-a389-17e6b8b9e0a8)

### O(1) 

* Accessing Array Index (int a = ARR[5];)
* Inserting a node in Linked List
* Pushing and Poping on Stack
* Insertion and Removal from Queue
* Finding out the parent or left/right child of a node in a tree stored in Array
* Jumping to Next/Previous element in Doubly Linked List

### O(n) 

* Traversing an array
* Traversing a linked list
* Linear Search
* Deletion of a specific element in a Linked List (Not sorted)
* Comparing two strings
* Checking for Palindrome
* Counting/Bucket Sort and here too you can find a million more such examples....

### O(log n)

* Binary Search
* Finding largest/smallest number in a binary search tree
* Certain Divide and Conquer Algorithms based on Linear functionality
* Calculating Fibonacci Numbers - Best Method The basic premise here is NOT using the complete data, and reducing the problem size with every iteration

### O(n log n)

* Merge Sort
* Heap Sort
* Quick Sort
* Certain Divide and Conquer Algorithms based on optimizing O(n^2) algorithms

### O(n^2) 
These ones are supposed to be the less efficient algorithms if their O(nlogn) counterparts are present. The general application may be Brute Force here.

* Bubble Sort
* Insertion Sort
* Selection Sort
* Traversing a simple 2D array

![BIG O](https://github.com/user-attachments/assets/038c2251-6b97-45f3-abed-bb9f81d24974)


Source:
* [Big O cheatSheet](https://www.bigocheatsheet.com/)
