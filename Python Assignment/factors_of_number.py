# Factors of number

num = int(input('Enter a number: '))

factor_list = []

for i in range(1,num+1):
    if num % i == 0:
        factor_list.append(i)
        # print(i)

print(f'The factors of {num} are {factor_list}')



# if len(factor_list) == 2:
#     print('It is a prime number')








'''
Enter a number: 16
The factors of 16 are [1, 2, 4, 8, 16]
'''  


# for i in range(1,int(num ** 0.5)+1):
#     if num % i == 0:
#         factor_list.append(i)
#         if i != num // i:
#             factor_list.append(num // i)

# factor_list.sort()
# print(f'The factors of {num} are {factor_list}')
