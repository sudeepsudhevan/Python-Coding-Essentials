# Armstrong number or not
num = int(input('Enter a Number: '))

checking_no = num
sum = 0

while num > 0:
    remainder = num % 10
    sum = sum + remainder ** 3
    num //=10                   # floor division num = num // 10

if sum == checking_no:
    print(f'{checking_no} is a Armstrong number')
else:
    print(f'{checking_no} is not a Armstrong number')






# num = str(num)

# for i in num:
#     sum += int(i) ** 3





'''
Enter a Number: 111
111 is not a Armstrong number

Enter a Number: 153
153 is a Armstrong number
'''