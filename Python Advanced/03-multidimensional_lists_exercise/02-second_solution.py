rows, columns = [int(el) for el in input().split()]
def read_matrix(rows,columns):
    matrix = []
    for row_count in range(rows):
            numbers = input().split()
            matrix.append(numbers)

    return matrix


def is_equal(matrix, rows, cols):
    left_upper_element = matrix[rows][cols]
    right_upper_element = matrix[rows][cols+1]
    left_lower_element = matrix[rows+1][cols]
    right_lower_element = matrix[rows+1][cols+1]

    if left_upper_element == right_upper_element == left_lower_element == right_lower_element:
        return True
    return False



matrix = read_matrix(rows, columns)

counter = 0
for row_index in range(rows-1):
    for column_index in range(columns-1):
        if is_equal(matrix, row_index, column_index):
            counter += 1

print(counter)