import sys
n = int(input())
total_sum = 0
max_num = -sys.maxsize


for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    total_sum += number

other_sum = total_sum - max_num
diff = abs(max_num - total_sum)
if other_sum == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    sum_others = abs(other_sum - max_num)
    print(f'Diff = {sum_others}')
