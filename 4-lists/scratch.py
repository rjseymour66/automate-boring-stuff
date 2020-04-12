# # Negative indexes

# spam = ['cat', 'bat', 'rat', 'elephant']

# spam[-1] # elephant
# print(spam[-1])

# # Slices

# spam[1:3]
# print(spam[1:3])

# # length

# print(len(spam))

# *********************************** For loops ***********************************

# for i in range(4):
#     print(i)

# for i in [5, 4, 3, 2, 1]:
#     print(i)

# supplies = ["pens", "staplers", "flamethrowers", "binders"]
# for i in range(len(supplies)):
#     print("Index " + str(i) + " in supplies is: " + supplies[i])

# *********************************** in and not in ***********************************

# spam = ['hello', 'hi', 'howdy', 'heyas']

# 'dog' in spam

# *********************************** Enumerate ***********************************

# supplies = ["pens", "staplers", "flamethrowers", "binders"]

# for index, item in enumerate(supplies):
#     print('Index ' + str(index) + ' in supplies is: ' + item)

# *********************************** random.choice() .shuffle() ***********************************

# import random 
# supplies = ["pens", "staplers", "flamethrowers", "binders"]

# print(random.choice(supplies))

# random.shuffle(supplies)
# for i in range(len(supplies)):
#     print(str(i) + ': ' + supplies[i])


# ********************** index() append() insert() remove() sort() reverse() ********************************

# supplies = ["pens", "staplers", "flamethrowers", "binders"]

# a = supplies.index('flamethrowers')
# print(a)

# supplies.append('daggers')
# for i in supplies:
#     print('Item: ' + str(supplies.index(i)) + ' ' + i)

# supplies.insert(2, 'duct tape')
# for i in supplies:
#     print('Item: ' + str(supplies.index(i)) + ' ' + i)

# supplies.remove('duct tape')
# for i in supplies:
#     print(i)

# numbers = [3, 6, 2, 7, 2, 1, 9, 11]

# for i in numbers:
#     print('Number: ' + str(i))


# numbers.sort()
# for i in numbers:
#     print('Number: ' + str(i))

# numbers.sort(reverse=True)
# for i in numbers:
#     print('Reverse: ' + str(i))

# *********************************** tuples, id ***********************************

eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))


type(('hello',))
type('hello')

a = id('Howdy')
print(a)