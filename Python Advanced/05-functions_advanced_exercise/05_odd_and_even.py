def check_command(command, even_nums, odd_nums, initial_list_length):
    result = 0
    if command == 'Odd':
        result = sum(odd_nums) * initial_list_length

    elif command == 'Even':
        result = sum(even_nums) * initial_list_length

    return result


command = input()
numbers = [int(el) for el in input().split()]
even_numbers = list(filter(lambda x: x % 2 ==0, numbers))
odd_numbers = list(filter(lambda x: x % 2 ==1, numbers))
print(check_command(command, even_numbers, odd_numbers, len(numbers)))