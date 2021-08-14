from players import Players
from actions import moves

board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '}

win_moves = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))



def handle(chose_position):
    select_position = None
    while select_position in board:
        position = input(chose_position)
        position = int(position)
        board[position] = Players.name
        return (select_position, Players.name)
    else:
        return position


def full_board():
    for i in board:
        print(i, '|', board[i], ' ', end='')
        if i % 3 == 0:
            print()

def check_empty_space(board, n):
    for i in board:
        for j in i:
            if j == n:
                return False
    return True


def check_game_result(game_board):

    for i in win_moves:
        pass