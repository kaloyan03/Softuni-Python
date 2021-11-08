rows, columns = [int(el) for el in input().split()]
def read_matrix(rows,columns):
    matrix = []
    for row_count in range(rows):
            numbers = input().split()
            matrix.append(numbers)

    return matrix


def check_if_indices_is_valid(matrix, row1,col1,row2,col2):
    if 0 <= row1 < len(matrix) and 0 <= col1 < len(matrix[0]) and 0 <= row2 < len(matrix) and 0 <= col2 < len(matrix[0]):
        return True
    return False



matrix = read_matrix(rows, columns)


command_input = input()
while not command_input == 'END':
    data = command_input.split()
    command = data[0]
    if command == 'swap' and len(data) == 5:
        rows1 = int(data[1])
        cols1 = int(data[2])
        new_rows = int(data[3])
        new_cols = int(data[4])
        if check_if_indices_is_valid(matrix,rows1,cols1,new_rows,new_cols):
            temp = matrix[rows1][cols1]
            matrix[rows1][cols1] = matrix[new_rows][new_cols]
            matrix[new_rows][new_cols] = temp
            for r in range(rows):
                print(f"{' '.join([str(el) for el in matrix[r]])}")
        else:
            print(f"Invalid input!")

    else:
        print(f"Invalid input!")
    command_input = input()

