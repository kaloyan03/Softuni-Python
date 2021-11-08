numbers = [int(el) for el in input().split()]
print(list(filter(lambda x: x% 2 == 0, numbers)))
