def check_if_move_is_in_bound(move, row_move, col_move, matrix, all_moves):
    if move[0] + row_move >= 0 and move[0] + row_move < len(matrix) and move[1] + col_move >= 0 and col_move + move[
        1] < len(matrix[0]):
        return True
    return False


rows, columns = list(map(int, input().split()))
matrix = []
curr_player_row = 0
curr_player_col = 0
for _ in range(rows):
    matrix.append([x for x in input()])

for rows_index in range(rows):
    if 'P' in matrix[rows_index]:
        curr_player_col = matrix[rows_index].index('P')
        curr_player_row = rows_index
        break

commands = input()
moves = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
its_over = False
has_won = False
for command in commands:
    next_row = moves[command][0]
    next_col = moves[command][1]
    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
        next_element = matrix[next_row][next_col]
        if next_element == 'B':
            its_over = True

        matrix[curr_player_row][curr_player_col] = '.'
        curr_player_row = next_row
        curr_player_col = next_col
        matrix[next_row][next_col] = 'P'

    else:
        has_won = True
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            element = matrix[row_index][col_index]
            if element == 'B':
                for command, move in moves.items():
                    if check_if_move_is_in_bound(move, row_index, col_index, matrix, moves):
                        if not matrix[row_index + move[0]][col_index + move[1]] == 'B':
                            matrix[row_index + move[0]][col_index + move[1]] = 'b'
                        if matrix[row_index+move[0]][col_index+move[1]] == 'P':
                            its_over = True
                            break

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            el = matrix[row_index][col_index]
            if el == 'b':
                matrix[row_index][col_index] = 'B'

    if its_over:
        break

    if has_won:
        break
if its_over:
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            print(matrix[row_index][col_index], end='')
        print()

    print(f"dead: {curr_player_row} {curr_player_col}")

if has_won:
    matrix[curr_player_row][curr_player_col] = '.'
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            print(matrix[row_index][col_index], end='')
        print()

    print(f"won: {curr_player_row} {curr_player_col}")
