from random import randint

DICE_MAX_NUMBER = 6
DICE_MIN_NUMBER = 1


number_of_dices = int(input('Please, enter the number of dices you want to roll.'))

counter = 0

result_messages = []

while counter != number_of_dices:
    counter += 1
    current_dice_number = randint(DICE_MIN_NUMBER, DICE_MAX_NUMBER)
    result_messages.append(f'Number of the dice {counter} is {current_dice_number}')


print(', '.join(result_messages))


