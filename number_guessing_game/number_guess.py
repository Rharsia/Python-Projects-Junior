import random

while True:
    number = random.randint(0,100)
    number_of_guesses = 0

    while True:
        guess = input("Guess the number: ")
        number_of_guesses += 1

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input, try again.")
            continue

        if number == guess:
            print(f"Congratulations! You guessed the correct number {number} and used {number_of_guesses} guesses")
            break
        else:
            if guess < number:
                result = "low"
            elif guess > number:
                result = "big"
            print(f"That's not right, your number is too {result}.")
            print("Guess again")
        
    print()
    input("Press any key to start a new game.")
    print()