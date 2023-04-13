import random

def menu():
    print("Options:")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")

def choice():
    menu()
    print()
    
    while True:
        pchoice = int(input("Enter your choice (1-3): "))

        if pchoice == 1:
            player = "rock"
            break
        elif pchoice == 2:
            player = "paper"
            break
        elif pchoice == 3:
            player = "scissor"
            break
        else:
            print("Invalid input, please try again.")

    return player

def evaluation(player_choice):
    options = ["rock", "paper", "scissor"]
    pc_choice = random.choice(options)

    if pc_choice == "rock":
        if player_choice == "rock":
            result = "draw"
        elif player_choice == "paper":
            result = "win"
        elif player_choice == "scissor":
            result = "lose"
    elif pc_choice == "paper":
        if player_choice == "rock":
            result = "lose"
        elif player_choice == "paper":
            result = "draw"
        elif player_choice == "scissor":
            result = "win"
    elif pc_choice == "scissor":
        if player_choice == "rock":
            result = "win"
        elif player_choice == "paper":
            result = "lose"
        elif player_choice == "scissor":
            result = "draw"

    return (result, player_choice, pc_choice)


def game():
    no_wins = 0
    no_losses = 0

    while True:
        player_choice = choice()
        print()

        result = evaluation(player_choice)

        if result[0] == "win":
            print("Win!")
            no_wins += 1
        elif result[0] == "draw":
            print("Draw!")
        elif result[0] == "lose":
            print("Loss!")
            no_losses += 1
        print(f"You played {result[1]}, pc played {result[2]}")
        

        print(f"Wins: {no_wins}; Losses: {no_losses}")
        print()

game()


