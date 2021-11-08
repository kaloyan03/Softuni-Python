def get_number_occurrences(line):
    occurrences_dict = {}
    for num in line:
        occurrences_dict[num] = line.count(num)

    return occurrences_dict


def numbers_searching(*args):
    sorted_numbers = sorted(args)
    duplicates = []
    numbers_occurrences = get_number_occurrences(sorted_numbers)

    for key, value in numbers_occurrences.items():
        if value != 1:
            duplicates.append(key)
    start_num = duplicates[0]
    end_num = duplicates[-1]
    missing_number = []
    for num in range(start_num,end_num + 1):
        if not num in duplicates:
            missing_number.append(num)
            missing_number.append(duplicates)
            break

    return missing_number

print(numbers_searching(1, 2, 4, 2, 5, 4))