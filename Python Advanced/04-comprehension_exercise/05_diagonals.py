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
            matr.append([int(el) for el in input().split(', ')])

    return matr

def primary_diagonal(matr):
    first_diagonal = []
    size = len(matr)
    the_sum = 0
    for i in range(size):
        first_diagonal.append(matr[i][i])
        the_sum += matr[i][i]
    return the_sum, first_diagonal


def secondary_diagonal(matr):
    second_diagonal = []
    the_sum = 0
    col = len(matr[0]) - 1
    for rows in range(len(matr)):
        the_sum += matr[rows][col]
        second_diagonal.append(matr[rows][col])
        col -= 1
    return the_sum, second_diagonal

matrix = read_matrix(is_test=False)
primary_diagonal_sum , first_diagonal = primary_diagonal(matrix)
secondary_diagonal_sum, second_diagonal = secondary_diagonal(matrix)

print(f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {primary_diagonal_sum}")
print(f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {secondary_diagonal_sum}")
