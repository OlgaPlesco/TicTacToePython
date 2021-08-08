board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '}


def print_board():
    for i in board:
        print(i, '|', board[i], ' ', end='')
        if i % 3 == 0:
            print()



