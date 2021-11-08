def read_matrix(is_test):
    if is_test:
        curr_matrix = [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, - 12],

        ]
        return curr_matrix
    else:
        curr_matrix = []
        size = int(input())
        for r in range(size):
            numbers = list(map(int, input().split()))
            curr_matrix.append(numbers)
        return curr_matrix

def primary_diagonal_sum(curr_matrix):
    size = len(curr_matrix)
    primary_sum = 0
    for i in range(size):
        primary_sum += curr_matrix[i][i]

    return primary_sum


def secondary_diagonal_sum(curr_matrix):
    size = len(curr_matrix)
    secondary_sum = 0
    for i in range(size - 1, -1 ,-1):
        secondary_sum += matrix[i][size - i - 1]
    return secondary_sum


def difference_between_sums(first_sum, second_sum):
    difference = abs(first_sum - second_sum)
    print(difference)
matrix = read_matrix(is_test=False)
primary_sum = primary_diagonal_sum(matrix)
secondary_sum = secondary_diagonal_sum(matrix)
diff = difference_between_sums(primary_sum, secondary_sum)

