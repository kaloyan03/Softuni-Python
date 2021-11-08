board_size = 8


def read_matrix(size):
    matrix = []
    king = []
    for rows in range(board_size):
        elements = input().split()
        if 'K' in elements:
            king.append(rows)
            king.append(elements.index('K'))

        matrix.append(elements)

    return matrix, king


def check_is_valid(length, row, col):
    if 0 <= row < length and 0 <= col < length:
        return True
    return False


def queen_movements(matrix,row,col):
    possible_moves_row = [-1, -1, 1, -1, 0, 0, 1, 1]
    possible_moves_col = [1, -1, 0, 0, 1, -1, 1, -1]
    is_found = False
    for i in range(len(possible_moves_col)):
        current_position_row = row + possible_moves_row[i]
        current_position_col = col + possible_moves_col[i]
        coordinates = []
        if not check_is_valid(len(matrix), current_position_row, current_position_col):
            continue
        while True:
            if matrix[current_position_row][current_position_col] == 'Q':
                break
            elif matrix[current_position_row][current_position_col] == 'K':
                coordinates.append(row)
                coordinates.append(col)
                is_found = True

                return coordinates

            current_position_row += possible_moves_row[i]
            current_position_col += possible_moves_col[i]
            if not check_is_valid(len(matrix), current_position_row, current_position_col):
                break




board, king_location = read_matrix(board_size)
coord = []
for rows_count in range(board_size):
    for columns_count in range(board_size):
        if board[rows_count][columns_count] == 'Q':

           coord.append(queen_movements(board,rows_count,columns_count))
counter = 0
for el in coord:
    if el != None:
        counter += 1
        print(el)

if counter == 0:
    print("The king is safe!")