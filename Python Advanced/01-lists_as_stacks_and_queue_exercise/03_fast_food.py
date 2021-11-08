from collections import deque

quantity_day = int(input())

orders = deque(list(map(int, input().split())))
max_order = max(orders)

while orders:
    order = orders.popleft()
    if order < quantity_day:
        quantity_day -= order

    else:

        orders.appendleft(order)

        break
#
if orders:
    print(f"Orders left:", end=" ")
    print(*orders)
else:
    print("Orders complete")