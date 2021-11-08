def read_matrix(is_test):
    curr_matrix = []
    if is_test:
        curr_matrix = [
            [8, 3, 2, 5],
            [6, 4, 7, 9],
            [9, 9, 3, 6],
            [6, 8, 1, 2],

        ]


    else:
        matrix_size = int(input())

        for _ in range(matrix_size):
            elements = list(map(int, input().split()))
            curr_matrix.append(elements)

    return curr_matrix


matrix = read_matrix(is_test=False)
coordinates_data = input().split()
coordinates = []

all_moves = {'up': [-1, 0], 'left_diagonal_up': [-1, -1], 'right_diagonal_up': [-1, +1], 'left': [0, -1],
             'right': [0, +1], 'down': [1, 0], 'left_diagonal_down': [1, -1], 'right_diagonal_down': [1, 1]}

for el in coordinates_data:
    data = el.split(',')
    row = int(data[0])
    col = int(data[1])
    coordinates.append(row)
    coordinates.append(col)

for index in range(0, len(coordinates), 2):
    row_bomb = coordinates[index]
    col_bomb = coordinates[index + 1]
    max_rows = len(matrix) - 1
    max_cols = len(matrix[0]) - 1
    curr_number = matrix[row_bomb][col_bomb]
    moves = []
    is_one_of_these = True
    if row_bomb == 0 and col_bomb == 0:
        moves.append(all_moves['down'])
        moves.append(all_moves['right_diagonal_down'])
        moves.append(all_moves['right'])
        is_one_of_these = False

    elif row_bomb == 0 and col_bomb == max_cols:
        moves.append(all_moves['down'])
        moves.append(all_moves['left'])
        moves.append(all_moves['left_diagonal_down'])

        is_one_of_these = False
    elif row_bomb == max_rows and col_bomb == 0:
        moves.append(all_moves['up'])
        moves.append(all_moves['right'])
        moves.append(all_moves['right_diagonal_up'])
        is_one_of_these = False
    elif row_bomb == max_rows and col_bomb == max_cols:
        moves.append(all_moves['up'])
        moves.append(all_moves['left'])
        moves.append(all_moves['left_diagonal_up'])
        is_one_of_these = False


    if is_one_of_these:
        if row_bomb == 0:
            moves.append(all_moves['down'])
            moves.append(all_moves['left_diagonal_down'])
            moves.append(all_moves['right'])
            moves.append(all_moves['left'])
            moves.append(all_moves['right_diagonal_down'])
        elif col_bomb == 0:
            moves.append(all_moves['up'])
            moves.append(all_moves['down'])
            moves.append(all_moves['right_diagonal_down'])
            moves.append(all_moves['right_diagonal_up'])
            moves.append(all_moves['right'])

        elif row_bomb == max_rows:
            moves.append(all_moves['up'])
            moves.append(all_moves['left_diagonal_up'])
            moves.append(all_moves['right'])
            moves.append(all_moves['left'])
            moves.append(all_moves['right_diagonal_up'])

        elif col_bomb == max_cols:
            moves.append(all_moves['up'])
            moves.append(all_moves['down'])
            moves.append(all_moves['left_diagonal_down'])
            moves.append(all_moves['left_diagonal_up'])
            moves.append(all_moves['left'])

        else:
            moves.append(all_moves['down'])
            moves.append(all_moves['up'])
            moves.append(all_moves['left_diagonal_down'])
            moves.append(all_moves['left_diagonal_up'])
            moves.append(all_moves['left'])
            moves.append(all_moves['right'])
            moves.append(all_moves['right_diagonal_up'])
            moves.append(all_moves['right_diagonal_down'])



    for iteration in moves:
        matrix[row_bomb][col_bomb] = 0
        number = matrix[row_bomb + iteration[0]][col_bomb + iteration[1]]
        if not number <= 0:
            matrix[row_bomb + iteration[0]][col_bomb + iteration[1]] -= curr_number


    print()


the_sum = 0
alive_cells = 0
for rows_index in range(len(matrix)):
    for column_index in range(len(matrix[0])):
        element = matrix[rows_index][column_index]
        if element > 0:
            alive_cells += 1
            the_sum += element


print(f"Alive cells: {alive_cells}")
print(f"Sum: {the_sum}")
for rows_index in range(len(matrix)):
    for column_index in range(len(matrix[0])):
        element = matrix[rows_index][column_index]
        if element > 0:
            alive_cells += 1
            the_sum += element
        print(matrix[rows_index][column_index], end=' ')
    print()