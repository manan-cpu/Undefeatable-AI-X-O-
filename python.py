import random

# Initialize board
board = [' ' for _ in range(9)]
player_symbol = 'X'
ai_symbol = 'O'

def print_board():
    """Display the 2D Tic-Tac-Toe board."""
    print("\n")
    print("     1   2   3")
    print("   -------------")
    print(" A |", board[0], "|", board[1], "|", board[2], "|")
    print("   -------------")
    print(" B |", board[3], "|", board[4], "|", board[5], "|")
    print("   -------------")
    print(" C |", board[6], "|", board[7], "|", board[8], "|")
    print("   -------------\n")

def reset_board():
    """Reset the board for a new game."""
    global board
    board = [' ' for _ in range(9)]

def is_board_full():
    """Check if the board is full."""
    return ' ' not in board

def is_winner(symbol):
    """Check if a player has won."""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == symbol:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == symbol:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True

    return False

def player_move():
    """Handle the player's move."""
    while True:
        move = input("Enter your move (e.g., A1, B3): ").upper()
        if len(move) == 2 and move[0] in "ABC" and move[1] in "123":
            row = "ABC".index(move[0])
            col = int(move[1]) - 1
            position = row * 3 + col
            if board[position] == ' ':
                board[position] = player_symbol
                break
            else:
                print("That position is already taken. Try again.")
        else:
            print("Invalid input. Use format like A1 or B3.")

def minimax(is_maximizing):
    """Implement the Minimax algorithm for optimal AI play."""
    if is_winner(ai_symbol):
        return 1
    if is_winner(player_symbol):
        return -1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_symbol
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player_symbol
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def ai_move():
    """Handle the AI's move using the Minimax algorithm."""
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_symbol
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = ai_symbol

def play_game():
    """Play the Tic-Tac-Toe game."""
    print("\nWelcome to 2D Tic-Tac-Toe!")
    print("You are 'X', and the AI is 'O'.")
    print("To make a move, enter the position (e.g., A1, B3).")
    print_board()

    # AI starts first
    ai_move()
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner(player_symbol):
            print("Congratulations! You won!")
            break
        if is_board_full():
            print("It's a tie!")
            break
        ai_move()
        print_board()
        if is_winner(ai_symbol):
            print("You lost! The AI won.")
            break
        if is_board_full():
            print("It's a tie!")
            break

def main():
    """Main function to run the game and handle retries."""
    while True:
        play_game()
        retry = input("Do you want to play again? (yes/no): ").lower()
        if retry == 'yes':
            reset_board()
        else:
            print("Thanks for playing! Goodbye!")
            break

main()
