DEFAULT_ROWS_COUNT = 7
DEFAULT_COLUMNS_COUNT = 7

def read_board(rows=DEFAULT_ROWS_COUNT, columns=DEFAULT_COLUMNS_COUNT):
    curr_matrix = []

    for row_index in range(rows):
        curr_matrix.append(input().split())
    return curr_matrix



def check_if_is_in_range_board(max_rows, max_cols, row, col):
    if 0 <= row < max_rows and 0 <= col < max_cols:
        return True
    return False


def get_corresponding_numbers_sum(board, row, col):
    moves = {'up': [1,0], 'down' :[-1,0], 'left': [0,-1], 'right': [0,1]}
    numbers = []
    row_element_position = row
    col_element_position = col
    for move, coord in moves.items():
        curr_move_row = coord[0]
        curr_move_col = coord[1]
        row = row_element_position
        col = col_element_position
        while True:
            row = row + curr_move_row
            col = col + curr_move_col
            if not check_if_is_in_range_board(len(board), len(board[0]), row, col):
                number = board[row-curr_move_row][col-curr_move_col]
                numbers.append(int(number))
                break

    return sum(numbers)

def print_result(name, throws):
    print(f"{name} won the game with {throws} throws!")



first_player_name, second_player_name = input().split(', ')
player_one_score, player_two_score = 501, 501
player_on_turn = 1
throws_counter_first_player = 1
throws_counter_second_player = 1
board = read_board()
coordinate = input()

while coordinate:
    coordinate_data = coordinate.split(', ')
    row = int(coordinate_data[0][1:])
    column = int(coordinate_data[1][:1])

    if check_if_is_in_range_board(len(board), len(board[0]), row, column):
        element_from_the_board = board[row][column]
        if element_from_the_board.isdigit():
            if player_on_turn == 1:
                player_one_score -= int(element_from_the_board)
            else:
                player_two_score -= int(element_from_the_board)

        elif element_from_the_board == 'D':
            the_sum = get_corresponding_numbers_sum(board, row, column) * 2
            if player_on_turn == 1:
                player_one_score -= int(the_sum)
            else:
                player_two_score -= int(the_sum)
        elif element_from_the_board == 'T':
            the_sum = get_corresponding_numbers_sum(board, row, column) * 3
            if player_on_turn == 1:
                player_one_score -= int(the_sum)
            else:
                player_two_score -= int(the_sum)

        elif element_from_the_board == 'B':
            if player_on_turn == 1:
                print_result(first_player_name, throws_counter_first_player)
            else:
                print(second_player_name, throws_counter_second_player)

            break


    if player_on_turn == 1:
        throws_counter_first_player += 1
        player_on_turn = 2
    else:
        throws_counter_second_player += 1
        player_on_turn = 1
    coordinate = input()

    if player_one_score <= 0:
        print_result(first_player_name, throws_counter_first_player-1)
        break
    elif player_two_score <= 0:
        print_result(second_player_name, throws_counter_second_player-1)
        break


