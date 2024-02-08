# Find the average of N numbers using for loop

num = int(input('Enter how many number to be entered: '))

sum = 0

print('Enter the numbers: ')
for i in range(0,num):
    sum += int(input())

average = sum/num

print(f'The average of the above {num} number is {average:.2f}')

















'''
Enter how many number to be entered: 4
Enter the numbers: 
13
10
12
11
The average of the above 4 number is 11.50
'''