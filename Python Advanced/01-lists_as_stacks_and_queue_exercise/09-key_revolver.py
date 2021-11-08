from collections import deque
bullet_price = int(input())
size_gun_barrel = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())
gun_barrel = deque()
is_first = True
money_spend = 0
counter = 0
bullet_used = 0
while len(bullets) > 0:
    if counter % size_gun_barrel == 0:
        if not counter == 0:
            print(f"Reloading!")
    counter += 1
    if not locks:
        break

    curr_bullet = bullets.pop()
    bullet_used += 1

    curr_lock = locks[0]

    if curr_bullet <= curr_lock:
        locks.popleft()
        print('Bang!')

    else:
        print('Ping!')
money_spend = bullet_price * bullet_used

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - money_spend}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
