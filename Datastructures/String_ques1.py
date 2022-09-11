
# wap to count all the character in a string
# and display the out like
 # a-3
from string import ascii_lowercase
str=" My name is ram gopal i am doing master of computer application"
for char in ascii_lowercase:
    print(f'{char}-{str.count(char)}')
