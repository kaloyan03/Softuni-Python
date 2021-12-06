from project.board import Board
from project.player import Player

# The game will be played until certain conditions - when there is no space left, or when there is a winner - diagonal, vertical, horizontal
# It will start with a while cycle in setup function in which we will be making base logic
# In board class we will be filling the fields which user has chosen, or if field is already filled, the user will need to select another field
# In player class we will get user move

def setup(is_test = False):
    if is_test:
        player1 = Player('Siyana', 1)
        player2 = Player('Kaloyan', 2)
    else:
        player_1_name = input(f'Welcome player 1, what\'s your name?\n')
        player_2_name = input(f'Welcome player 2, what\'s your name?\n')
        player1 = Player(player_1_name, 1)
        player2 = Player(player_2_name, 2)

    board = Board(player1, player2)
    board.create_board()

    player_on_turn = 1

    board.read_matrix()

    while True:
        # main logic
        if player_on_turn == 1:
            player_move = player1.play_turn()
            if not board.validate_move(player_move):
                continue



            current_player_sign = player1.player_sign
            current_player_name = player1.name
        else:
            player_move = player2.play_turn()

            if not board.validate_move(player_move):
                continue
            current_player_sign = player2.player_sign
            current_player_name = player2.name


        board.fill_field(player_move, current_player_sign)
        board.read_matrix()

        if (board.check_if_winner()):
            print(f'{current_player_name} has won!')
            break

        if (board.check_if_all_fields_are_filled() == True):
            print('There is no winner!')
            break

        player_on_turn = 1 if player_on_turn == 2 else 2
setup(is_test=False)