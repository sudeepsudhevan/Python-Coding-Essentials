# Program to print squares of all numbers in a list

list_length = int(input('Enter how many number in the list: '))

list = []
print('Enter the numbers in the list: ')
for i in range(list_length):
    list.append(int(input()))

print(f'User Entered list: {list}')

sqr_list = []
for i in list:
    sqr_list.append(i**2)
    

print(f'Squared list:  {sqr_list}')
















'''
Enter how many number in the list: 6
Enter the numbers in the list: 
11
12
6
4
9
8
User Entered list: [11, 12, 6, 4, 9, 8]
Squared list:  [121, 144, 36, 16, 81, 64]
'''