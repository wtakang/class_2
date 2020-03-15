person = dict(name='chris',
           city='seattle', 
           cake='chocolate')
print('question 1. create and print a dictionary')
print(person)
print()

print('question 1a. remove an item form the above dictionary and print the dictionary')
removed_item = person.pop('cake')#remove the item 'cake'
print(person)
print()
print('the item removed is\n',removed_item)
print()

print('question 1b. add an item to the above dictionary and display')
person['fruit']='mango'#add the fruit mango to the dictionary
print(person)
print()

print('question 1c. display the "keys" of the dictionary')
print(person.keys())
print()

print('question 1d. display the values of the above "keys"')
print(person.values())
print()

print('question 1e. cake in dictionary?')
print('cake' in person.keys())
print()

print('check if "mango" in dictionary')
print('mango' in person.values())
#print('mango' in man.items())
for item in person.items(): # loop via the items of the dictionary
    if 'mango' in item: #check if 'mango' exist in every item of the dictionary
        print('True', item)
print()

print('question 2')
numbers = [i for i in range(16)] #store a range of numbers from 1-15
hexs = []
for i in range(10):
    hexs.append(i)
for j in 'ABCDEF':
    hexs.append(j) # add the letters 'ABCDEF' to the end of the 'hexs' list
num_hexs = {}
for numbers, hexs in zip(numbers, hexs): #use the zip function to create a dictionary using the two lists
    num_hexs[numbers]=hexs
print(num_hexs)
print()

print('question 3.')
#boy = dict(name='tanyi', age=20, likes='games')
#print(len(man['name']))
for value in person: # loop via the dictionary of above
    a = len(person[value])# get the lenght of each value 
    person[value]= 'a'*a #set the value of each item to its equivilent number of 'a's
print(person)
print()

print('question 4.')

numbers = [i for i in range(21)]
print('the original list is:\n',numbers)
print()
lista = [] 
listb = []
listc = []
for number in numbers:
    if number == 0:
        continue
    if number % 2 == 0:
        lista.append(number) # add the value in the 'a' list
    if number % 3 == 0:
        listb.append(number) # add the value in the 'b' list
    if number % 4 == 0:
        listc.append(number) # add the value in the 'c' list

s2 = set(lista) #convert all the lists to sets
s3 = set(listb)
s4 = set(listc)

print('set 2 is: \n',s2)
print('set 3 is: \n',s3)
print('set 4 is: \n',s4)
print()

print(s3.issubset(s2))
print()

print(s4.issubset(s2))
print()

print('question 5')
b = 'Python' + 'i'
c = 'marathon'
ns = set(b)
fs = frozenset(c)
print()
print('the union of both sets is:' ,ns.union(fs))
print()
print('the intersection of both sets is:' ,ns.intersection(fs))

# print('question 6')
# def safe_input():
#     user = input('type in somthing' )
#     return user

# try:
#    safe_input()
# except EOFError:
#     print('end of file')
print()

print('queation 7a')
import os
currentdir = os.getcwd()
files_in_dir = os.listdir(currentdir)
for file in files_in_dir:
    print(file, os.path.abspath(file))
print()

print('question 7b')
file_to_copy = os.path.abspath(files_in_dir[len(files_in_dir)-2])# selected a particular file to copy
print('the file to be copied is \n',file_to_copy)
# copy_dir = chdir(r'/home/tanyi/development/pythonclass')
# os.popen('cp file_to_copy copy_dir')
#cp file_to_copy copy_dir
print()

print('question 8')
names = ['tanyi', 'besong', 'ayuk']
textfiles = [name+'.txt' for name in names] #create thier corresponding text files
msg = 'hello'
for name in range(len(names)):
    with open(textfiles[name], 'a') as f: #create and add the texts below into the individual text files
        f.write(msg+' {}. we write to inform you that, due to...!'.format(names[name]))
  
for textfile in textfiles:
    with open(textfile, 'r') as f:
        print(f.read()) #read and print the files
          
print()