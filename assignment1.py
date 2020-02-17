#this program Print the sum of 2 numbers
def sum(a, b):
    print(a+b)

sum(3+4)

#this program Print the difference of 2 numbers
def difference(a, b):
    print(a-b)

difference(5-3)

#write 3 lines of code that ask a user for their name, stores the name and
#prints it out

def getuser():
    print('please type in your name!')
    name = input()
    print(name)

getuser()

#Define two variables and print them
a = 6
c = 3.14
print(a, c)

#Define two variables and print them using concatenation
a = 4
b = 'tanyi'
print('my name is '+b+' and i am '+str(a))

#Which of the following are operators, and which are values?
operators (-, /, +, *)
values  ('hello', -88.8, 5)

#What is an expression made up of? What do all expressions do?
'expresssions are made up of a combination of values and operators and expressions return a value."

#This chapter introduced assignment statements, like spam = 10 . What is
#the difference between an expression and a statement?

"an expression returns a value while a statement does not"

#What does the variable bacon contain after the following code runs?
#    bacon = 20
#    bacon + 1

bacon = 21

#Why is eggs a valid variable name while 100 is invalid?
"this is because variable names don't begin with a number!"

#What three functions can be used to get the integer, floating-point
#number, or string version of a value?
int() to get integer
str() to get strings
float() to get floats

#Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
'because we are try to join a string value and an interger value. that gives the error'
"the solution is to convert the integer value to string first."
'I have eaten ' + str(99) + ' burritos.'

def collatz(number):
    if number % 2 == 0:
        print( number // 2)
        return number
    else number % 2 == 1:
        print((number* 3 ) + 1)
     
#Then write a program that lets the user type in an integer and that keeps
#calling collatz() on that number until the function returns the value 1

userguess = int(input('please type in a number ' ))
while True:
    collatz(userguess):
    if ccollatz(userguess) == 1:
        break
     
     
     