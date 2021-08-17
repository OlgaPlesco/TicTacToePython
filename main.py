from actions import yes_or_no
from actions import moves
from players import Players
from actions import flip_players
from actions import game_moves
from players import x_game_moves
from players import y_game_moves
from actions import check_win
from actions import check_position


def game():
    play_or_not = yes_or_no("Do you want to play?")


    if play_or_not == "y":
        print("Game started.\n")
        moves()
        check_win()

        while len(game_moves) != 9:

            if check_win() is False:
                flip_players()
                print(game_moves, x_game_moves, y_game_moves)
                check_win()
            else:
                print(f"Congratulations, {Players.current_player_mark}!")
                break
        else:
            print("draw")


    else:
        print(f"Bye, {Players.name}!")

def regame():
    replay_or_not = yes_or_no("Would you repete the experience?")
    if replay_or_not == "y":
        return game()
    else:
        print(f"Bye, {Players.name}!")

if __name__ == '__main__':
    game()
    regame()
