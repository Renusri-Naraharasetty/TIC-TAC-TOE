import random

# Define the game board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")
    print("\n")

# Function to check if the game is over (win or tie)
def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
            return board[condition[0]]  # Returns 'X' or 'O' if there's a winner
    if " " not in board:
        return "Tie"  # The game is a tie if no empty spaces are left
    return None  # The game is still ongoing

# Function for player turn
def player_turn(player, symbol):
    while True:
        try:
            move = int(input(f"Player {player} ({symbol}), enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = symbol
                break
            else:
                print("The spot is already taken, choose another spot.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")
    print_board()

# Function for computer turn
def computer_turn(symbol):
    print("Computer is making a move...")
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = symbol
            break
    print_board()

# Main game loop
def play_game():
    print_board()
    while True:
        player_turn(1, 'X')  # Player 1 is X
        winner = check_win()
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"Player {1} wins!")
            break

        computer_turn('O')  # Computer is O
        winner = check_win()
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"Computer wins!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
