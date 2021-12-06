class Board:
    def __init__(self, player1, player2):
        self.__fields = 3
        self.player1 = player1
        self.player2 = player2
        self.__field_mapper = {
            1: [0,0],
            2: [0,1],
            3: [0,2],
            4: [1,0],
            5: [1,1],
            6: [1,2],
            7: [2,0],
            8: [2,1],
            9: [2,2],
        }
        self.__filled_fields = []

    def create_board(self):
        matrix = []
        counter = 1
        for row in range(self.__fields):
            matrix.append([])
            for col in range(self.__fields):
                matrix[row].append(counter)
                counter += 1
        self.board = matrix

    def read_matrix(self):
        if not self.board:
            print('Your board isn\'t initialized yet!')
        for row in self.board:
            print(' | '.join([str(el) for el in row]))

    def fill_field(self, field_number, player_sign):
        self.__filled_fields.append(field_number)
        board_coord = self.__field_mapper[field_number]
        row = board_coord[0]
        col = board_coord[1]
        self.board[row][col] = player_sign

    def check_if_all_fields_are_filled(self):
        empty_spaces = 0
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board[0])):
                if self.board[row_index][col_index] not in ['O', 'X']:
                    empty_spaces += 1

    def check_if_winner(self):
        if (self.check_winner_horizontal() or self.check_winner_vertical() or self.check_winner_primary_diagonal() or self.check_winner_secondary_diagonal()):
            # End the game
            return True

    def check_winner_horizontal(self):
        for row_index in range(len(self.board)):
            if self.board[row_index][0] == self.board[row_index][1] == self.board[row_index][2]:
                return True

    def check_winner_vertical(self):
        for col_index in range(len(self.board[0])):
            row_index = 0
            if self.board[row_index][col_index] == self.board[row_index + 1][col_index] == self.board[row_index + 2][col_index]:
                return True


    def check_winner_primary_diagonal(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

    def check_winner_secondary_diagonal(self):
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

    def validate_move(self, field_number):
        if (field_number in self.__filled_fields):
            print('Number you entered is not valid, please check the table with numbers again, and select one that is valid!')
            return False
        return True


