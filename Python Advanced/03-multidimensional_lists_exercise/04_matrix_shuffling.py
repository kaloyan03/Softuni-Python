def read_matrix(is_test):
    if is_test:
        curr_matrix = [
            [1, 2, 3],
            [4, 5, 6],

        ]
        return curr_matrix
    else:
        curr_matrix = []
        (   rows_count, columns_count) = list(map(int, input().split()))
        for r in range(rows_count):
            elements_to_add = input().split()
            curr_matrix.append(elements_to_add)
        return curr_matrix


def is_valid_coord(row , col, curr_matrix):
    if 0 <= row and row < len(curr_matrix) and 0 <= col and col <= len(curr_matrix):
        return True
    return False

matrix = read_matrix(is_test=False)
command_input = input()

while not command_input == 'END':
    data = command_input.split()
    coordinates = data[1:]
    command = data[0]
    rows = len(matrix)
    cols = len(matrix[0])
    if command == 'swap' and len(coordinates) == 4:
        for index in range(0, len(coordinates), 2):
            row = int(coordinates[index])
            col = int(coordinates[index+1])
            if not is_valid_coord(row, col , matrix):
                print(f"Invalid input!")
                break

            else:
                if not index == 2:
                    row_to_swap = row
                    col_to_swap = col
                else:
                    temp = matrix[row][col]

                    matrix[row][col] = matrix[row_to_swap][col_to_swap]
                    matrix[row_to_swap][col_to_swap] = temp
                    for row_index in range(len(matrix)):
                        for col_index in range(len(matrix[row_index])):
                            print(f"{matrix[row_index][col_index]}", end=' ')
                        print()

    else:
        print("Invalid input!")

    command_input = input()
