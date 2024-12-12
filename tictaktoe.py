# Function to print the Tic-Tac-Toe board
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Function to check if someone has won
def check_win(values, player):
    # Check rows, columns, and diagonals
    win_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # First column
        [1, 4, 7],  # Second column
        [2, 5, 8],  # Third column
        [0, 4, 8],  # Diagonal (top-left to bottom-right)
        [2, 4, 6]   # Diagonal (top-right to bottom-left)
    ]
    for combination in win_combinations:
        if values[combination[0]] == values[combination[1]] == values[combination[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_full(values):
    return " " not in values

# Main game function
def play_game():
    values = [" "] * 9  # Empty board
    current_player = "X"  # X starts first

    while True:
        print_tic_tac_toe(values)
        print(f"Player {current_player}'s turn")

        # Get user input
        try:
            move = int(input(f"Enter position (1-9) for {current_player}: ")) - 1
            if move < 0 or move > 8 or values[move] != " ":
                print("Invalid move, try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        # Place the player's move
        values[move] = current_player

        # Check for a winner
        if check_win(values, current_player):
            print_tic_tac_toe(values)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_full(values):
            print_tic_tac_toe(values)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
