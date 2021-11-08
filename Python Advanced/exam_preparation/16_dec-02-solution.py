def check_is_valid_indices(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def print_result(matrix, letters):
    print(letters)

    for rows in range(len(matrix)):
        for cols in range(len(matrix[0])):
            print(matrix[rows][cols], end='')
        print()

letters = input()
field_size = int(input())
field = []
player_position_row = 0
player_position_col = 0



for rows_count in range(field_size):
    rows = [x for x in input()]
    field.append(rows)
    if 'P' in rows:
        player_position_row = rows_count
        player_position_col = rows.index('P')
commands_count = int(input())
moves = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

for _ in range(commands_count):
    command = input()
    move = moves[command]
    row_move = player_position_row + move[0]
    col_move = player_position_col + move[1]
    if check_is_valid_indices(len(field), row_move, col_move):
        if field[row_move][col_move] != '-':
            letters += field[row_move][col_move]
        field[player_position_row][player_position_col] = '-'
        player_position_row = row_move
        player_position_col = col_move
        field[row_move][col_move] = 'P'
    else:
        if letters:
            letters = letters[:-1]

print_result(field,letters)
