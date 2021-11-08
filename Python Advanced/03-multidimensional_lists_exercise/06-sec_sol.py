board_size = int(input())


def read_board(size):
    matrix = []

    for _ in range(board_size):
        matrix.append([el for el in input()])

    return matrix


def is_valid_indices(row,col,curr_position_row, curr_position_col,size,matrix):
    pass


def check_kills_count(matrix, row, col):
    possible_moves_row = [1, 2, 1, 2, -1, -2, -1, -2]
    possible_moves_col = [2, 1, -2, -1, 2, 1, 2, 2]
    kills = 0
    for iteration in range(len(possible_moves_row)):
        if is_valid_indices(possible_moves_row[iteration],possible_moves_col[iteration], board_size, board):
            pass


board = read_board(board_size)
killer_position = []


for row in range(len(board)):
    for col in range(len(board[0])):
        element = board[row][col]
        if element == 'K':
            check_kills_count(board, row, col)
