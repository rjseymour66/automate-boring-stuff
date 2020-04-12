import random, sys 

print('ROCK, PAPER, SCISSORS')

# vars that store the wins, losses, ties 
wins = 0
losses = 0
ties = 0 

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # the player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print('Fine, asshole - fuck you!')
            sys.exit() # quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break out of the input loop 
        print('Type one of r, p, s, or q.') # if they don't type a correct option

    # display the player choice
    if playerMove == 'r':
        print('ROCK vs...')
    elif playerMove == 'p':
        print('PAPER vs...')
    elif playerMove == 's':
        print('SCISSORS vs...')
    
    # Display what the computer chose 
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

        # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

# Setting PATH for Python 2.7
# The original version is saved in .bash_profile.pysave
# PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"
# export PATH

# Setting PATH for Python 3.7
# The original version is saved in .bash_profile.pysave
# PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
# export PATH