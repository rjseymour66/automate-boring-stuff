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