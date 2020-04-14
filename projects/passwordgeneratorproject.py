#creating a password generator in python

import random

#characters will be alpanumerical and more
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFEGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+=-,./;[]{}'
#number and length of password will be integers
number = int(input('number of passwords? -'))
length = int(input('length of password? -'))

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(characters)
print(password)
