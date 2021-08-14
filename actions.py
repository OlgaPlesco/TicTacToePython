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
    if first_move_choice == "y":
        print("Ok, do your first move with X.\n")
        you.set_mark("X")
        print(you.name, you.mark)
    else:
        print("Ok, wait to be the second to chose your move with O.\n")
        you.set_mark("O")
        print(you.mark)
