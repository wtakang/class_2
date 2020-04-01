# this program generates a password in python

import random
def password(l=8):
    # this string contains all the characters needed to build a strong password
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#_'
    password = '' # an empty string to hold the password
    
    for i in range(l):
        password += random.choice(characters) # randomly select from characters and save in password
    return password

try:
    # collect a number to use as length of password from keyboard
    length = int(input('type a number greater than eight for the length of your password!\n' ))
except ValueError:
    # if user enters a non-digit
    length = 8 #set the length to default as used in the password function above
    print('using the default password length') # inform the user of the use of the default length
    print()
    print(password(length))   
else:
    # print a password of length as requested by the user
    print()
    print('printing a password as long as you requested!')
    print(password(length)) 