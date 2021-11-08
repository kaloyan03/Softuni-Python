matrix_size = int(input())
commands = input().split()


def read_matrix(n, is_test):
    curr_matrix = []
    if is_test:
        curr_matrix = [
            ['*', '*', '*', 'c', '*'],
            ['*', '*', '*', 'e', '*'],
            ['*', '*', 'c', '*', '*'],
            ['s', '*', '*', 'c', '*'],
            ['*', '*', 'c', '*', '*'],

        ]

    else:

        for _ in range(n):
            elements = input().split()
            curr_matrix.append(elements)

    return curr_matrix


def check_is_valid_bound(matr, position):
    rows = position[0]
    columns = position[1]
    if 0 <= rows < len(matr) and 0 <= columns < len(matr):
        return True
    return False


matrix = read_matrix(matrix_size, is_test=False)
coals_counter = 0
starting_position = []
curr_position = []
for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        element = matrix[row_index][column_index]
        if element == 'c':
            coals_counter += 1
        if element == 's':
            starting_position.append(row_index)
            starting_position.append(column_index)

curr_position_row = starting_position[0]
curr_position_col = starting_position[1]
is_over = False
for command in commands:
    next_move_row = 0
    next_move_col = 0
    next_position = []

    if command == 'up':
        next_move_row -= 1
        next_position = [curr_position_row + next_move_row, curr_position_col]
    elif command == 'down':
        next_move_row += 1
        next_position = [curr_position_row + next_move_row, curr_position_col]
    elif command == 'right':
        next_move_col += 1
        next_position = [curr_position_row, curr_position_col + next_move_col]
    elif command == 'left':
        next_move_col -= 1
        next_position = [curr_position_row, curr_position_col + next_move_col]

    if check_is_valid_bound(matrix, next_position):

        next_element = matrix[next_position[0]][next_position[1]]

        if next_element == 'c':
            matrix[curr_position_row][curr_position_col] = '*'
            curr_position_row = next_position[0]
            curr_position_col = next_position[1]
            matrix[curr_position_row][curr_position_col] = 's'
            coals_counter -= 1
            if coals_counter <= 0:
                print(f"You collected all coals! ({next_position[0]}, {next_position[1]})")
                is_over = True
                break

        elif next_element == 'e':
            print(f"Game over! ({next_position[0]}, {next_position[1]})")
            is_over = True
            break

        else:
            matrix[curr_position_row][curr_position_col] = '*'
            curr_position_row = next_position[0]
            curr_position_col = next_position[1]
            matrix[curr_position_row][curr_position_col] = 's'


if not is_over:
    print(f"{coals_counter} coals left. ({curr_position_row}, {curr_position_col})")
