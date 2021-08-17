import players
from players import Players
from players import x_game_moves
from players import y_game_moves
from board import win_moves


game_moves = []
position = None


def yes_or_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def moves():
    first_move_choice = yes_or_no(f"{Players.name}, do you want to do the first move?")
    you = players.Players()

    if first_move_choice == "y":
        position = input("Ok, do your first move with X.\n")
        you.set_mark ( "X" )
        #        print(you.name, you.mark)
        Players.current_player_mark = you.mark
        #       print(Players.current_player_mark)
        game_moves.append ( position )
        x_game_moves.append(position)
        print (len(game_moves))
  #           game_moves.append (position)
    else:
        position = input("Ok, wait to be the second to chose your move with O.\n")
        you.set_mark("O")
#        print(you.mark)
        Players.current_player_mark = you.mark
#        print(Players.current_player_mark)
        game_moves.append ( position )
        y_game_moves.append(position)
        print (len(game_moves))


def flip_players():
    position = input ("Do another move please.\n")
    if Players.current_player_mark == "X":
        Players.current_player_mark = "O"
        game_moves.append(position)
        y_game_moves.append(position)

    elif Players.current_player_mark == "O":
        Players.current_player_mark = "X"
        game_moves.append(position)
        x_game_moves.append(position)


def check_position():
    for i in game_moves:
        if position is None:
            continue
        elif any(elem in position for elem in i):
            print("Position selected already.")
            return position







def check_win():
    for list in win_moves:
        if all(elem in x_game_moves for elem in list) or all(elem in y_game_moves for elem in list):
            return True
        else:
            return False




