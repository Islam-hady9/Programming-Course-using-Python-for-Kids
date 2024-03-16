import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = int(input("Guess the number between 1 and 100: "))

    while guess != number:
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Try again: "))

    print("Congratulations! You guessed the number", number)

guess_the_number()
