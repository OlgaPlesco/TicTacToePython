from board import full_board
from actions import yes_or_no
from actions import moves
from players import get_player_details



def game():
    play_or_not = yes_or_no ("Do you want to play?")

    if play_or_not == "y":
        print ("Game started.\n")
        get_player_details(first_player_list=True, second_player_list=False)
        # current_player = player_details[0]
        # player_details = get_player_details(current_player)
        moves()
    else:
        print("Bye!")


if __name__ == '__main__':
  game()