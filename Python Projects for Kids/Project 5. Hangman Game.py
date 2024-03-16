import random

def hangman():
    words = ["apple", "banana", "orange", "grape", "strawberry"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", "".join(letter if letter in guessed_letters else "_" for letter in word))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess!")
            attempts -= 1
            print("Attempts left:", attempts)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("Game over! The word was:", word)

hangman()
