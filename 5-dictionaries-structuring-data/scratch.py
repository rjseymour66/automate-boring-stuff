# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# print(myCat['size'])

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated')

# ********************************** keys() values() items() **********************************

# spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#     print(v)

# for k in spam.keys():
#     print(k)

# # get() method
# picnicItems = {'apples': 5, 'cups': 2}

# print(str(picnicItems.get('cups', 0))) # key of the value you want to retrieve, fallback number if it isn't there
# print(str(picnicItems.get('eggs', 0)))

# ********************************** setDefault() **********************************

# looks for the key. If it is not there, adds the key and the second value in the parentheses

# spam = {'name': 'Pooka', 'age': 5}
# spam.setdefault('color', 'black')


# ********************************** Pretty Printing *****************************************

# import pprint  # prints dictionary values in a clean way

# message = "It was a bright cold day in April, and the clocks were striking thriteen."

# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# pprint.pprint(count)

# ********************************** Nested dictionaries and lists *****************************************

allGuests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))