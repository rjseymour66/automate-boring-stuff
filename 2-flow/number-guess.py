# Number guessing game

import random 

secretNumber = random.randint(0, 21)

print('Guess a number between 1 and 20')

# Ask player to guess 6 times 

for guessesTaken in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low. Try again.')
    elif guess > secretNumber:
        print('Your guess is too high. Try again.')
    else:
        break # they guessed the number 

if guess == secretNumber:
    print('Yay! You guessed the number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Sorry - you didn\'t guess the correct number.')