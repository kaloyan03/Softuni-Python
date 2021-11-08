n, m = list(map(int, input().split()))
first_set_nums = []
second_set_nums = []

for _ in range(n):
    first_set_nums.append(int(input()))

for _ in range(m):
    second_set_nums.append(int(input()))
result = []
for el in first_set_nums:
    if el in second_set_nums:
        result.append(el)

for el in second_set_nums:
    if el in first_set_nums:
        result.append(el)

result = set(result)
for el in result:
    print(el)