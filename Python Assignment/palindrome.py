# Palindrome

word = input('Enter a Word or Number for check it is a Palindrome: ').lower()

# if word == word[::-1]:
#     print(f'Above word {word} is a Palindrome')
# else:
#     print(f'Above word {word} is not a Palindrome')

reversed_string = ''

for letter in word:
    reversed_string = letter + reversed_string 

# print(reversed_string)

if word == reversed_string:
    print(f'Above word {word} is a Palindrome')
else:
    print(f'Above word {word} is not a Palindrome')













'''
Enter a Word or Number for check it is a Palindrome: rotor
Above word rotor is a Palindrome
'''