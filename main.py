from actions import yes_or_no
from actions import moves
from players import Players
from actions import flip_players
from actions import game_moves
from players import x_game_moves
from players import y_game_moves
from actions import check_win



def game():
    play_or_not = yes_or_no("Do you want to play?")

    if play_or_not == "y":
        print("Game started.\n")
        moves()
        check_win()
        while len(game_moves) != 9:
            flip_players()
            print(game_moves, x_game_moves, y_game_moves)
            check_win()
        else:

            print("nn")

    else:
        print(f"Bye, {Players.name}!")


if __name__ == '__main__':
    game()
