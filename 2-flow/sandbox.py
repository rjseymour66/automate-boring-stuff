# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

# # for loop
# # need 'for' variable 'in'

# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

# total = 0
# for num in range(101):
#     total = total + num 
# print(total)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(5, -1, -1):
#     print(i)

# ******************************************************************************************

# IMPORTING MODULES 

# import random

# for i in range(5):
#     print(random.randint(1, 10))

# IMPORTING SPECIFIC FUNCS IN LIBRARIES
# don't need 'random' prefix to 'randint' now


# from random import *

# for i in range(5):
#     print(randint(1, 10))

# ******************************************************************************************
# TERMINATE PROGRAM WITH sys

import sys 

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')