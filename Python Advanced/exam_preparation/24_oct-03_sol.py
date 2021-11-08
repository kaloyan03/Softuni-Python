from collections import deque
def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    best_sum = 0
    best_sum_rotation = 0
    for rotation in range(k+1):
        curr_sum = 0
        if not rotation == 0:
            numbers.rotate(1)
        for i in range(len(numbers)):
            num = numbers[i]
            curr_sum += num * i
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_sum_rotation = rotation

    result = f'Best pureness {best_sum} after {best_sum_rotation} rotations'
    return result

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
