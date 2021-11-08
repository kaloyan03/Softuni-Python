from collections import deque

n = int(input())

data = deque([])

for _ in range(n):
    data.append([el for el in input().split()])



for big_circle in range(n):
    is_valid = True
    tank_petrol = 0
    for small_circle in range(n):
        petrol = int(data[small_circle][0])
        distance_next_station = int(data[small_circle][1])
        tank_petrol += petrol - distance_next_station

        if tank_petrol < 0:
            is_valid = False
            data.append(data.popleft())
            break

    if is_valid:
        print(big_circle)
        break