class Player:
    player_signs = ['X', 'O']

    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number
        self.player_sign = self.select_player_sign()

    def select_player_sign(self):
        if self.player_number == 1:
            while True:
                player_sign = input(f'Hey {self.name}, select sign - {Player.player_signs[0]} or {Player.player_signs[1]}\n').upper()
                if not self.validate_player_sign(player_sign):
                    continue
                break
        else:
            player_sign = Player.player_signs[0]
            print(f'{self.name} your sign will be {player_sign}')

        Player.player_signs.remove(player_sign)
        return player_sign

    def player_greeting(self):
        print(f'Hello, {self.name}!')


    def play_turn(self):
        player_choose = int(input(f'It\'s your turn, {self.name}, select empty position from 1-9'))
        return player_choose

    def validate_player_sign(self, sign):
        if sign not in Player.player_signs:
            print("The sign you entered isn\'t valid")
            return False
        return True

