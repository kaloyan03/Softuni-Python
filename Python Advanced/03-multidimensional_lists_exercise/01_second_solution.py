matrix_size = int(input())
def read_matrix(size):
    matrix = []
    for row_count in range(size):
        numbers = [int(el) for el in input().split()]
        matrix.append(numbers)

    return matrix


def primary_diagonal_sum(matrix,size):
    the_sum = 0
    for i in range(size):
            the_sum += matrix[i][i]
    return the_sum


def secondary_diagonal_sum(matrix, size):
    the_sum = 0
    column_index = size - 1
    for row_index in range(size):
        num = matrix[row_index][column_index]
        the_sum += num
        column_index -= 1
    return the_sum


def print_result(primary_d_sum, secondary_d_sum):
    diff = abs(primary_d_sum - secondary_d_sum)
    print(diff)

matrix = read_matrix(matrix_size)
sum_primary_diagonal = primary_diagonal_sum(matrix,size=matrix_size)
sum_secondary_diagonal = secondary_diagonal_sum(matrix, size=matrix_size)
print_result(sum_primary_diagonal, sum_secondary_diagonal)