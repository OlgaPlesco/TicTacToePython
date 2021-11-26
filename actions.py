from players import Players, x_game_moves, y_game_moves
from board import win_moves

n = [1, 2, 3]
game_moves = []





def pn(asq_position):
    insert_position = None
    while insert_position not in n:
        insert_position = int(input(asq_position))
#    return insert_position

def yes_or_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def moves():
    first_move_choice = yes_or_no(f"{Players.name}, do you want to do the first move?")
    you = Players()

    def position():
        position = None
        try:
            position = int(input("Insert a number,please."))
        except ValueError:
            return position

    if first_move_choice == "y":
        move_position = position()
        # move_position("Ok dodod")
        # move_position = int(input("Ok, do your first move with X.\n"))
        you.set_mark ("X")
        #        print(you.name, you.mark)
        Players.current_player_mark = you.mark
        #       print(Players.current_player_mark)
        game_moves.append (move_position)
        x_game_moves.append(move_position)
        print (len(game_moves))
  #           game_moves.append (position)
    else:
        position = int(input("Ok, wait to be the second to chose your move with O.\n"))
        you.set_mark("O")
#        print(you.mark)
        Players.current_player_mark = you.mark
#        print(Players.current_player_mark)
        game_moves.append (position)
        y_game_moves.append(position)
        print (len(game_moves))


def flip_players():
    position = int(input ("Do another move please.\n"))
    while position not in game_moves:
        if Players.current_player_mark == "X":
            Players.current_player_mark = "O"
            # check_position()
            game_moves.append(position)
            y_game_moves.append(position)

        elif Players.current_player_mark == "O":
            Players.current_player_mark = "X"
            # check_position()
            game_moves.append(position)
            x_game_moves.append(position)
    return position


def check_position():
    # for i in game_moves:
    #     if position is None:
    #         continue
    #     elif any(elem in position for elem in i):
    #         print("Position selected already.")
    #         return position
    tried_moves = None
    while tried_moves in game_moves:
        return position
    pass






def check_win():
    for list in win_moves:
        if all(a in x_game_moves for a in list) or all(b in y_game_moves for b .+
                                                       in list):
            return True
        else:
            return False







