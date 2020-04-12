```python
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# for loop
# need 'for' variable 'in'

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num 
print(total)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

# ******************************************************************************************

# IMPORTING MODULES 

import random

for i in range(5):
    print(random.randint(1, 10))

# IMPORTING SPECIFIC FUNCS IN LIBRARIES
don't need 'random' prefix to 'randint' now


from random import *

for i in range(5):
    print(randint(1, 10))

# ******************************************************************************************
# TERMINATE PROGRAM WITH sys

import sys 

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

# *********************************** Functions *********************************************

# def hello(name):
#     print('Hello, ' + name)

# hello('Ryan!')

# None = null in java
# spam = print('hello')

# print('Hello', end=' ')
# print('World')

# GLOBAL STATEMENT

def spam():
    global eggs # in this function, eggs refers to the global variable, so don't create a local variable with this name
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# ************************************* EXCEPTION HANDLING *************************************

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


# OR

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument')

# ************************************* Lists *************************************


# ********************** index() append() insert() remove() sort() reverse() ********************************

supplies = ["pens", "staplers", "flamethrowers", "binders"]

a = supplies.index('flamethrowers')
print(a)

supplies.append('daggers')
for i in supplies:
    print('Item: ' + str(supplies.index(i)) + ' ' + i)

supplies.insert(2, 'duct tape')
for i in supplies:
    print('Item: ' + str(supplies.index(i)) + ' ' + i)

supplies.remove('duct tape')
for i in supplies:
    print(i)

numbers = [3, 6, 2, 7, 2, 1, 9, 11]

for i in numbers:
    print('Number: ' + str(i))


numbers.sort()
for i in numbers:
    print('Number: ' + str(i))

numbers.sort(reverse=True)
for i in numbers:
    print('Reverse: ' + str(i))

# *********************************** tuples, id ***********************************

eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))


type(('hello',))
type('hello')

a = id('Howdy')
print(a)

```