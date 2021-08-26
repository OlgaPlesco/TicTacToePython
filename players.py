x_game_moves = []
y_game_moves = []


class Players:
    name = input("Please type your name.    ")
    def current_player_mark(self, new_current_player_mark):
        self.current_player_mark = new_current_player_mark


#    def __init__(self, name, mark):
#        self.name = name
#        self.mark = mark


#    def get_name(self):
#        self.name = name
#        return self.name

    def set_name(self, new_name):
        self.name = new_name

#    def get_mark(self):
#        self.mark = mark
#        return self.mark

    def set_mark(self, new_mark):
        self.mark = new_mark

    def set_win_game_combination(self, new_win_game_combination):
        self.set_win_game_combination = new_win_game_combination

    def set_current_player_mark(self, new_current_player_mark):
        self.current_player_mark = new_current_player_mark




# def get_player_details(current_player):
#     first_player = ()
#     second_player =[]
#     first_player_list = []
#     second_player_list = []
#     current_player = ""
#     name = input("Please type your name.\n")
#     mark = input("Please select the mark to play with: X or O.")
# # winner_combination = ("")
#     if mark  == "x" or mark == "X":
#         first_player == current_player
#         first_player_list.append(name)
#         first_player_list.append(mark)
#     elif mark == "o" or mark == "O":
#         second_player == current_player
#         second_player_list.append(name)
#         second_player_list.append(mark)
#     else:
#         return mark == "x"
# ## print(first_player_list, second_player_list)
#     print("Nice to have you here, ", current_player, ". Your selected mark is ", mark,".\n")
#     print(current_player, name)
