# catName1 = 'Zophie'
# catName2 = 'Pooka'
# catName3 = 'Simon'
# catName4 = 'Lady Macbeth'
# catName5 = 'Fat-tail'
# catName6 = 'Miss Cleo'

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
    ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatentation
print('The cat names are:')
for name in catNames:
    print(' ' + name)