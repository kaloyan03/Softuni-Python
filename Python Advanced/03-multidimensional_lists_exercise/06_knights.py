def read_matrix(is_test):
    curr_matrix = []
    if is_test:
        curr_matrix = [
            ['0', 'K', '0', 'K', '0'],
            ['K', '0', '0', '0', 'K'],
            ['0', '0', 'K', '0', '0'],
            ['K', '0', '0', '0', 'K'],
            ['0', 'K', '0', 'K', '0'],

        ]


    else:
        matrix_size = int(input())

        for _ in range(matrix_size):
            curr_matrix.append(list(input()))

    return curr_matrix


matrix = read_matrix(is_test=False)

def is_valid_bound(row, col, length):
    if 0 <= row < length and 0 <= col < length:
        return True
    return False


def kills_count(row, col, matrix):
    curr_position = [row, col]
    knight_row_moves = [2, 1, 2, 1, -2, -1, -2, -1]
    knight_col_moves = [-1, -2, 1, 2, 1, 2, -1, -2]
    kills = 0

    for index in range(len(knight_row_moves)):
        potential_row = row + knight_row_moves[index]
        potential_col = col + knight_col_moves[index]
        if is_valid_bound(potential_row, potential_col,len(matrix)):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == 'K':
                kills += 1
    return kills
removed_counter = 0
while True:
    most_kills = 0
    killer_position = []
    for rows_index in range(len(matrix)):
        for cols_index in range(len(matrix[rows_index])):
            curr_el = matrix[rows_index][cols_index]
            if curr_el == 'K':
                kills = kills_count(rows_index, cols_index, matrix)
                if kills > most_kills:
                    most_kills = kills
                    killer_position = [rows_index, cols_index]

    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        removed_counter += 1
    else:
        break

print(removed_counter)