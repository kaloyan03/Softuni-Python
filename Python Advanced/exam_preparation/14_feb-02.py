from math import ceil
COINS_TO_WIN_GAME = 100
size = int(input())


def read_matrix(size, is_test=False):
    if is_test:
        curr_matrix = [
            ['1', 'X', '7', '9', '11'],
            ['X', '14', '46', '62', '0'],
            ['15', '33', '21', '95', 'X'],
            ['P', '14', '3', '4', '18'],
            ['9', '20', '33', 'X', '0'],

        ]
        return curr_matrix
    else:
        curr_matrix = []
        for row in range(size):

            elements = [x for x in input().split()]
            curr_matrix.append(elements)
        return curr_matrix

def print_result(won, total_coins, player_moves):
    if won:
        print(f"You won! You've collected {ceil(total_coins)} coins.")
    else:
        print(f"Game over! You've collected {ceil(total_coins // 2)} coins.")

    print("Your path:")
    for move in player_moves:
        print(move)


def check_next_position(max_rows, max_cols, current_row, current_col):
    if 0 <= current_row < max_rows and 0 <= current_col < max_cols:
        return True
    return False

def check_win_condition(coins, coins_to_win=COINS_TO_WIN_GAME):
    return coins >= coins_to_win


def run_while_condition(board, mapper, player_position):
    command = input()
    coins_collected = 0
    moves = []
    while True:
        if command in mapper:
            next_position = [player_position[0] + mapper[command][0], player_position[1] + mapper[command][1]]
            if check_next_position(len(board), len(board[0]), next_position[0], next_position[1]):
                element = board[next_position[0]][next_position[1]]
                if element.isdigit():
                    moves.append(next_position)
                    coins_collected += int(element)
                    if check_win_condition(coins_collected):
                        print_result(True, coins_collected, moves)
                        break
                else:


                    print_result(False, coins_collected, moves)
                    break

            else:
                print_result(False, coins_collected, moves)
                break

            player_position = next_position[0], next_position[1]


        command = input()


board = read_matrix(size)
command_mapper = {'up': [-1,0], 'down': [1,0], 'right':[0,1], 'left':[0,-1]}
player_position = []
for row_index in range(size):
    for col_index in range(size):
        if board[row_index][col_index] == 'P':
            player_position.append(row_index)
            player_position.append(col_index)

run_while_condition(board, command_mapper,  player_position)

