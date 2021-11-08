def get_ascii_value_sum(word):
    the_sum = 0
    for char in word:
        ascii_value = ord(char)
        the_sum += ascii_value

    return the_sum

n = int(input())
odd_numbers_set = set()
even_numbers_set = set()


for row in range(1, n + 1):
    name = input()
    ascii_value_sum = get_ascii_value_sum(name)
    the_sum = ascii_value_sum // row
    if the_sum % 2 == 0:
        even_numbers_set.add(the_sum)
    else:
        odd_numbers_set.add(the_sum)

if sum(odd_numbers_set) < sum(even_numbers_set):
    result = even_numbers_set.symmetric_difference(odd_numbers_set)


elif sum(odd_numbers_set) > sum(even_numbers_set):
    result = odd_numbers_set.difference(even_numbers_set)


else:
    result = even_numbers_set.union(odd_numbers_set)

print(', '.join(str(el) for el in result))