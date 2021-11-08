n = int(input())
elements = []
for _ in range(n):
    data = input().split()
    for el in data:
        elements.append(el)
elements = set(elements)
for el in elements:
    print(el)