# Q02a

from random import *

#  Initialise variables
counter = 1
answer = randint(1,9)
guess = 0


#  Print prompt and take guess from user
guess = int (input (f'Enter a number from 1 - 10: '))


#  Create WHILE loop to check if guess is correct

while (guess != answer):
    counter = counter + 1
    if guess > answer:
        guess = int(input (f'Guess was too high, try again with a lower one: '))
    if guess < answer:
        guess = int(input (f'Guess was too low, Try again with a higher one: '))



#  Report the correct answer to the user and indicate the number of guesses

print(f'Congrats!!! You guessed {guess} right in just {counter} attempts')
