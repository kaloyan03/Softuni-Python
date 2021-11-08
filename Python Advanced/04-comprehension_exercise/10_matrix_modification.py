def read_matrix(is_test):
    matr = []
    if is_test:
        matr = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    else:
        rows = int(input())
        for row_index in range(rows):
            matr.append([int(el) for el in input().split()])

    return matr


def check_if_index_is_valid(matrix ,matrix_row, matrix_col):
    if 0 <= matrix_row < len(matrix) and 0 <= matrix_col < len(matrix[0]):
        return True
    return False



def add_to_matrix(matrix, matrix_row, matrix_col, value):
    matrix[matrix_row][matrix_col] += value
    return matrix


def subtract_num_matrix(matrix,matrix_row, matrix_col, value):
    matrix[matrix_row][matrix_col] -= value
    return matrix


matrix = read_matrix(is_test=False)


def print_res(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end=' ')
        print()

command_input = input()

while not command_input == 'END':
    tokens = command_input.split()
    command = tokens[0]
    row = int(tokens[1])
    column = int(tokens[2])
    value = int(tokens[3])
    if check_if_index_is_valid(matrix, row, column):
        if command == 'Add':
            matrix = add_to_matrix(matrix,row,column,value)

        elif command == 'Subtract':
            matrix = subtract_num_matrix(matrix, row , column, value)
    else:
        print(f"Invalid coordinates")

    command_input = input()

print_res(matrix)