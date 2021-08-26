from actions import yes_or_no, moves, flip_players, game_moves, check_win
from players import Players, x_game_moves, y_game_moves


def game():
    play_or_not = yes_or_no("Do you want to play?")

    if play_or_not == "y":
        print("Game started.\n")
        moves()
        check_win()

        while len(game_moves) <= 9:

            if not check_win():
                flip_players()
                print(game_moves, x_game_moves, y_game_moves)
                check_win()
            else:
                print(f"Congratulations, {Players.current_player_mark}!")
                game_moves.clear()
                x_game_moves.clear()
                y_game_moves.clear()
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
    response = yes_or_no("First round is over. You can play more. Select Y or N.")
    while True:
        regame()
        break
