n = input().split()

s = []

for num in n:
    s.append(int(num))

while s:
    print(s.pop(), end=' ')
