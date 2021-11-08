def read_matrix(is_test):
    if is_test:
        curr_matrix = [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4],

        ]
        return curr_matrix
    else:
        curr_matrix = []
        (rows_count, columns_count) = list(map(int, input().split()))
        for r in range(rows_count):
            numbers = list(map(int, input().split()))
            curr_matrix.append(numbers)
        return curr_matrix

def getting_sum_of_3x3_matrix(curr_matrix , row, col):
    line = []
    sum_of_curr_matrix = 0
    curr_number = curr_matrix[row][col]
    line.append(curr_number)
    after_curr_number = curr_matrix[row][col+1]
    line.append(after_curr_number)
    after_after_curr_number = curr_matrix[row][col+2]
    line.append(after_after_curr_number)
    number_down_roll = curr_matrix[row+1][col]
    line.append(number_down_roll)
    number_after_down_roll = curr_matrix[row+1][col+1]
    line.append(number_after_down_roll)
    number_after_after_down_roll = curr_matrix[row+1][col+2]
    line.append(number_after_after_down_roll)
    number_down_down_rol = curr_matrix[row+2][col]
    line.append(number_down_down_rol)
    number_after_down_down_rol = curr_matrix[row+2][col+1]
    line.append(number_after_down_down_rol)
    number_after_after_down_down_rol = curr_matrix[row+2][col+2]
    line.append(number_after_after_down_down_rol)
    sum_of_curr_matrix = curr_number + after_curr_number + after_after_curr_number + number_down_roll + number_after_down_roll + number_after_after_down_roll + number_down_down_rol + number_after_down_down_rol + number_after_after_down_down_rol
    return sum_of_curr_matrix, line


def print_res(result, matrix):
    print(f"Sum = {result}")

    for i in range(len(matrix)):
        if i != 0:
            if i % 3 == 0:
                print()
        print(matrix[i], end=' ')



matrix = read_matrix(is_test=False)
biggest_sum , biggest_sum_matrix = getting_sum_of_3x3_matrix(matrix, 0, 0)

for rows_index in range(len(matrix) -2):
    for cols_index in range(len(matrix[0]) - 2):
        curr_sum, curr_matrix = getting_sum_of_3x3_matrix(matrix, rows_index , cols_index)
        if curr_sum > biggest_sum:
            biggest_sum = curr_sum
            biggest_sum_matrix = curr_matrix


print_res(biggest_sum, biggest_sum_matrix)
