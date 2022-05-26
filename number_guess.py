from random import randint
import math

lower = 3
upper = 20
limit = 10

x = randint (lower , upper)
print('\n\tYou\'ve only ',
       limit,
      ' chances to guess the integer!\n')
 
# for calculation of minimum number of
# guesses depends upon range
while limit != 0:
    limit-=1
    # taking guessing number as input
    guess = int(input('Guess a number:- '))
 
    # Condition testing
    if x == guess:
        print('Congratulations you did it in ',
              count, ' try')
        # Once guessed, loop will break
        break
    elif x > guess:
        print('You guessed too small!')
    elif x < guess:
        print('You Guessed too high!')
