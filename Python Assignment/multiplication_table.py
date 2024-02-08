# multiplication table

num = int(input('Enter multiplication table of: '))

for i in range(1,21):
    result = num * i
    print(f'{i} X {num} = {result}')