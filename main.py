from actions import yes_or_no
from actions import moves
from players import Players


def game():
    play_or_not = yes_or_no("Do you want to play?")

    if play_or_not == "y":
        print("Game started.\n")
        moves()
    else:
        print(f"Bye, {Players.name}!")


if __name__ == '__main__':
    game()
