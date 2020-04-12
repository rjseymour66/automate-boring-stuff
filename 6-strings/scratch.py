# ********************* Raw strings 

# print(r'That is Carol\'s cat')

# ********************* Multiline strings

# print('''Dear Alice, 

# Eve's cat has been arresting for catnapping, cat burglary, and extortion.

# Sincerely,

# Bob''')

# ********************* Multiline comments
# def spam():
#     """This is a multiline comment to help
#     explain what the spam() function does."""
#     print('Hello!')
# spam()


# ********************* Slicing strings 

spam = 'Hello, World!'

negative = spam[-1]
slice = spam[0:5]

print('negative ' + negative)
print('slice ' + slice)

# ********************* in and out

spam = 'Hello, World!'

'Hello' in spam

# ********************* upper() lower() isupper() islower()

spam = 'Hello, world!'

spam.upper()
spam.lower()
spam.isupper()
spam.islower()

# ********************* isX() methods

"""
isalpha() Returns True if the string consists only of letters and isn’t blank

isalnum() Returns True if the string consists only of letters and numbers and is not blank

isdecimal() Returns True if the string consists only of numeric characters and is not blank

isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank

istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
"""

# ********************* Remove whitespace strip() rstrip() lstrip()

# spam = '       Hello, World     '
# spam.strip()
# spam.lstrip()
# spam.rstrip()


# ********************* Copy Paste pyperclip 

import pyperclip

pyperclip.copy('Hello World')
pyperclip.paste()