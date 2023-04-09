# hangman game
import random

# list of words for the game
words = ["apple", "banana", "cherry", "date", "fig", "grape", "melon", "pineapple"]

while True:
    # randomly select a word
    word = random.choice(words)

    # create a list of underscores for each letter in the word
    display = ["_"] * len(word)

    # set the number of guesses
    guesses = 7

    # loop the game
    while guesses > 0 and "_" in display:
        # print the current state of the display
        print(display)

        letter = input("Guess a letter: ")

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    display[i] = letter
            print("Correct!")
            print()
            
        else:
            guesses -= 1
            print(f"Incorrect. You have {guesses} guesses left")
            print()

    # game over
    if "_" not in display:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of guesses. Word: {word}")

    # new game
    input()
    print("New Game?")
    answer = input("y/n: ")

    if answer == "n":
        break
    else:
        continue