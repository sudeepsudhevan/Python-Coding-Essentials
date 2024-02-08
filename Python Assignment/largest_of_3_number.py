# Find the Biggest of 3 numbers

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

if num1 == num2 == num3:
    print('All are same number')
elif num1 > num2 and num1 > num3:
    print(f'Largest number is {num1}')
elif num2 > num3:
    print(f'Largest number is {num2}')
else:
    print(f'Largest number is {num3}')    










'''
Enter the first number: 12
Enter the second number: 15
Enter the third number: 17
Largest number is 17
'''