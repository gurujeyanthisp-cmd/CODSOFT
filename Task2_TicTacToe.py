# Task 2 - Tic Tac Toe AI
# CodeSoft AI Internship

# Function to print the board
def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# Function to check winner
def check_winner(board, player):

    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == player and \
           board[combo[1]] == player and \
           board[combo[2]] == player:
            return True

    return False


# Function to check draw
def check_draw(board):
    return " " not in board


# AI move
def ai_move(board):

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


# Main Game
board = [" "] * 9

print("Welcome to Tic Tac Toe!")
print("You are X and AI is O")

while True:

    print_board(board)

    # Player move
    move = int(input("Enter your move (1-9): ")) - 1

    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move! Try again.")
        continue

    # Check player win
    if check_winner(board, "X"):
        print_board(board)
        print("Congratulations! You win!")
        break

    # Check draw
    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI move
    ai_move(board)

    # Check AI win
    if check_winner(board, "O"):
        print_board(board)
        print("AI wins!")
        break

    # Check draw again
    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break
