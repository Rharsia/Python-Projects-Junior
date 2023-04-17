# board function
def print_board(board):
    for i in range(3):
        print("+---+---+---+")
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
    print("+---+---+---+")

# check winner 
def check_winner(board):
    
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]
    
        # check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]
        
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[2][0] != "-":
        return board[0][2]
    
# game function
def play_game():
    # game start
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    player = "X"
    winner = None

    # game loop
    while winner is None:
        print_board(board)

        # player input
        row = int(input(f"Player {player}'s turn. Choose row (1-3): ")) - 1
        col = int(input(f"Player {player}'s turn. Choose column (1-3): ")) - 1

        # check if move is valid
        if board[row][col] != "-":
            print("Invalid move. Try again.")
            continue

        # make move
        board[row][col] = player

        # check winner
        winner = check_winner(board)

        # Switch players
        player = "O" if player == "X" else "X"

    # game over
    print_board(board)
    print(f"{winner} wins!")

play_game()