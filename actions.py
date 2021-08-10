from board import full_board

def yes_or_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def moves():
    first_move_choice = yes_or_no ("Do you want to do first move?")
    if first_move_choice == "y":
        print ("Do your first move.")
    else:
        print ("\nWait to be the second to chose your move.")
