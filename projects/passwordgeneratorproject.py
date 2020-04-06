import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFEGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+=-,./;[]{}'
number = int(input('number of passwords? -'))
length = int(input('length of password? -'))
for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(characters)
print(password)
