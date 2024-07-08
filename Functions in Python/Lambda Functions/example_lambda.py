my_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_numbers = list(filter(lambda x: x % 2 == 0, my_list)) # take elements where condition true
print(even_numbers)  # Output: [4, 6, 8, 12]

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(filter(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


my_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_numbers = list(map(lambda x: x % 2 == 0, my_list)) # take results where condition true
print(even_numbers)  # Output: [4, 6, 8, 12]

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
