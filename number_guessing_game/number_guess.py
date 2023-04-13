import random

number = random.randint(0,100)

while True:
    guess = input("Guess the number: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input, try again.")
        continue

    if number == guess:
        print(f"Congratulations! You guessed the correct number {number}")
        break
    else:
        if guess < number:
            result = "low"
        elif guess > number:
            result = "big"
        print(f"That's not right, your number is too {result}.")
        print("Guess again")