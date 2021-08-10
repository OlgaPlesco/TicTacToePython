from board import full_board
from actions import yes_or_no
from actions import moves


def game():
    play_or_not = yes_or_no ("Do you want to play?")

    if play_or_not == "y":
        print ("Game started.")
        moves()
    else:
        print("Bye!")


if __name__ == '__main__':
  game()