def check_if_fields_are_empty(*args):
    args_length = len(args)
    counter = 0
    is_filled = False
    while counter < args_length:
        if (args[counter] != ''):
            counter += 1
            continue
        break

    if counter == args_length:
        print('Fields are filled')
    else:
        print('Fields are not filled')


fields = ['Kaloyan', 'Sofia', 15, '18 school']

check_if_fields_are_empty('Kaloyan', '', 15, 'asd')