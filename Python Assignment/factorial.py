# Facorial of a number

num = int(input('Enter a number to find the factorial: '))

factorial = 0

if num == 0 or num == 1:
    factorial = 1
elif num > 1:
    factorial = 1
    for i in range(2, num+1):
        factorial = factorial * i

if num < 0:
    print('Factorial Does not exist for negative number.')
else:
    print(f'Factorial of {num} is {factorial}')  






'''
Enter a number to find the factorial: 6
Factorial of 6 is 720
'''


