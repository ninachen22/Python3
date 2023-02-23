from random import randrange

# Exercise 2
number = randrange(10)
guess = int(input('Guess a number between 0 and 10: '))
if guess < number:
    print('Your guess ' + str(guess) + ' was too low. The number was: ' + str(number))
elif guess > number:
    print('Your guess ' + str(guess) + ' was too high. The number was: ' + str(number))
else:
    print('Your guess ' + str(guess) + ' is correct! The number was: ' + str(number))
