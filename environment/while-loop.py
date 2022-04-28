#1 Working with a while loop
#Printing the game rules
print("Wlecome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#importing random and writing a while loop
import random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guess {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
        

