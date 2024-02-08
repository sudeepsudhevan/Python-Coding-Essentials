# Calculator using if elif

num1 = float(input('Enter the First Number: '))
operation = int(input('\n1. Addition            2. Substraction\n3. Multiplication      4. Divison\nEnter Corresponding number for the operation: '))
num2 = float(input('\nEnter the Second Number: '))

# calculate = f'{(num1)}{operation}{num2}'
# print(type(calculate))
# print(f'Result is: {eval(calculate)}')

result = 0

if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2
elif operation == 4:
    result = num1 / num2
    # remainder = num1 % num2
    # print(f'Remainder is: {remainder}')
else: 
    print('Wrong Input')

print(f'Result is {result}')












'''
Enter the First Number: 45

1. Addition            2. Substraction
3. Multiplication      4. Divison
Enter Corresponding number for the operation: 4

Enter the Second Number: 12
Remainder is: 9.0
Result is 3.75
'''