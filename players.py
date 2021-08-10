from actions import yes_or_no

def name_selection():
    mark_selection = yes_or_no ("Do you want to be Alfa and play X today?")
    if name_selection == "y":
        print ("Nice choise, Alfa. You will mark with X in this game.\n")
        current_player_list.append("Alfa")
    else:
        print ("Beta is also a nice nick. Don't forget that you mark with O.\n")
        current_player_list.append("Beta")

def get_player_details(first_player_list, second_player_list):
    first_player_list = []
    second_player_list = []
    name = input("Plase type your name.\n")
    mark = input("Please select the mark to play with: X or O.")
   # winner_combination = ("")
    if mark  == "x" or mark == "X":
      first_player_list.append(name)
      first_player_list.append(mark)
    else:
      second_player_list.append(name)
      second_player_list.append(mark)
   # print(first_player_list, second_player_list)
    print("Nice to have you here, ", name,". Your selected mark is ", mark,".\n")




