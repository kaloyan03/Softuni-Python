def read_matrix(is_test):
    if is_test:
        curr_matrix = [
            ['A', 'B', 'B', 'D'],
            ['E', 'B', 'B', 'B'],
            ['I', 'J', 'B', 'B'],

        ]
        return curr_matrix
    else:
        curr_matrix = []
        (rows_count, columns_count) = list(map(int, input().split()))
        for r in range(rows_count):
            numbers = input().split()
            curr_matrix.append(numbers)
        return curr_matrix

def if_is_equal(curr_matrix, row, col):
    curr_number = curr_matrix[row][col]
    next_col_number = curr_matrix[row][col+1]
    next_rol_number = curr_matrix[row+1][col]
    next_rol_number_left = curr_matrix[row+1][col+1]
    if curr_number == next_col_number and next_rol_number == next_rol_number_left and next_col_number == next_rol_number_left:
        return True
    return False


matrix = read_matrix(is_test=False)
counter = 0
for rows_index in range(len(matrix) - 1):
    for cols_index in range(len(matrix[0]) - 1):
        if if_is_equal(matrix, rows_index, cols_index):
            counter += 1

print(counter)