## 1. Bubble Sort
Repeatedly swaps adjacent elements if they are in the wrong order.

```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
my_array = [8, 2, 6, 4, 5]
sorted_array = bubble_sort(my_array)
print(sorted_array)
```

## 2. Selection Sort
Selects the smallest (or largest) element and places it in the correct position

```
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
my_array = [8, 2, 6, 4, 5]
sorted_array = selection_sort(my_array)
print(sorted_array)
```

## 3. Insertion Sort
Insertion Sort is a simple sorting algorithm that works by repeatedly taking an element from the unsorted part of the array and inserting it into its correct position in the sorted part

```
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
my_array = [8, 2, 6, 4, 5]
sorted_array = insertion_sort(my_array)
print(sorted_array)
```

## 4. Merge Sort
Merge Sort is a divide-and-conquer algorithm that breaks down an array into smaller subarrays, sorts them individually, and then merges them back together to create a sorted array

```
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Append remaining elements from both halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
my_array = [12, 11, 13, 5, 6, 7]
merge_sort(my_array)
print("Sorted array using Merge Sort:", my_array)

```

## 5. Quick Sort
Quick Sort is another efficient sorting algorithm based on partitioning

```
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_array = [12, 11, 13, 5, 6, 7]
sorted_array = quick_sort(my_array)
print("Sorted array using Quick Sort:", sorted_array)

```

## 6. Heap Sort
Heap Sort is a comparison-based sorting algorithm that leverages a binary heap data structure

```
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Example usage:
my_array = [12, 11, 13, 5, 6, 7]
heapSort(my_array)
print("Sorted array using Heap Sort:", my_array)

```

## 7. Linear Search
Linear search is the simplest searching algorithm. It sequentially checks each element of the list until it finds the target value

```
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = linear_search(arr, target)
if result != -1:
    print(f"Linear Search: Element found at index {result}")
else:
    print("Linear Search: Element not found")
```

## 8. Binary Search
Binary search is more efficient and suitable for sorted lists. It repeatedly divides the search interval in half until the target value is found

```
def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")

```

## 9. Ternary Search 
Ternary Search is used to find the maximum or minimum value of a unimodal function within a given range\

```
def ternary_search(func, left, right, absolute_precision=1e-9):
    while right - left > absolute_precision:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if func(mid1) < func(mid2):
            left = mid1
        else:
            right = mid2
    return (left + right) / 2

# Example usage:
def f(x):
    return -(x - 3) ** 2 + 5
max_x = ternary_search(f, 0, 5)
max_y = f(max_x)
print("Maximum value at x =", max_x, "with y =", max_y)

```

## 10. Jump Search
Jump Search is a searching algorithm for sorted arrays. It checks fewer elements than linear search by jumping ahead in fixed steps

```
def jump_search(arr, target):
    n = len(arr)
    step = int(n ** 0.5)  # Determine block size
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

# Example usage:
my_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target_value = 55
result = jump_search(my_array, target_value)
if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found")

```

## 11. Hash-based Search 
Hashing allows efficient lookups by mapping keys to indices. While Python provides built-in dictionaries (hash tables)

```
class HashTable:
    def __init__(self):
        self.table = [None] * 10  # Initialize with 10 slots

    def _hash(self, key):
        return hash(key) % len(self.table)

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index] = value

    def search(self, key):
        index = self._hash(key)
        return self.table[index]

# Example usage:
my_hash_table = HashTable()
my_hash_table.insert("apple", 42)
print("Value for key 'apple':", my_hash_table.search("apple"))

```

## 12. Binary Search Tree (BST)
A Binary Search Tree is a sorted binary tree where left child values are less than the root, and right child values are greater.

```
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Example usage:
bst_root = None
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for val in values:
    bst_root = insert(bst_root, val)
# Now you can perform search, deletion, and other BST operations

```
