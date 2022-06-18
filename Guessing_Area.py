import random
print("Welcome To Number Guessing Game ~!")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")
while chances < 5:
    guessedNumber =  int(input("Enter your guessed number:- "))
    if guessedNumber == number:
        print("Congratulations, You Won The Game ~!!")
        break
    elif guessedNumber < number:
        print("Your guessed number was too low! Make a higher guess than", guessedNumber)
    else:
        print("Your guessed number was too high! Make a lower guess than", guessedNumber)
    chances +=1
if not chances < 5:
    print("Uh oh! You lost:-( The number is", number)