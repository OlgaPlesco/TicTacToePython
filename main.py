from board import print_board
from players import get_player_details


def game():
    print("Welcome to Tic-Tac-Toe! Please select 1 to start the game or 0 to exit.")
    print("Here is your game board")
    print_board()
    print("Player {}, is your firs move. Please enter a number between 1 and 9.")

game()
