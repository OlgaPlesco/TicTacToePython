import players
from players import Players


def yes_or_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def moves():
    first_move_choice = yes_or_no(f"{Players.name}, do you want to do the first move?")
    you = players.Players()
    global position
    game_moves = []
    if first_move_choice == "y":
        position = input("Ok, do your first move with X.\n")
        you.set_mark("X")
#        print(you.name, you.mark)
        Players.current_player_mark = you.mark
 #       print(Players.current_player_mark)
        game_moves.append(position)
        print(game_moves)
    else:
        position = input("Ok, wait to be the second to chose your move with O.\n")
        you.set_mark("O")
#        print(you.mark)
        Players.current_player_mark = you.mark
#        print(Players.current_player_mark)


def flip_players():
    if Players.current_player_mark == "X":
        Players.current_player_mark = "O"
    elif Players.current_player_mark == "O":
        Players.current_player_mark = "X"
    return Players.current_player_mark