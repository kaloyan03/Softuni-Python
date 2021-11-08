from collections import deque
cups = deque([int(el) for el in input().split()])
bottles = [int(el) for el in input().split()]
wasted_water = 0
while cups and bottles:
    curr_bottle = bottles.pop()
    curr_cup = cups.popleft()

    curr_cup -= curr_bottle

    if curr_cup <= 0:
        wasted_water += abs(curr_cup)

    else:
        cups.appendleft(curr_cup)
if bottles:
    print(f"Bottles: {' '.join([str(el) for el in reversed(bottles)])}")

else:
    print(f"Cups: {' '.join([str(el) for el in cups])}")

print(f"Wasted litters of water: {abs(wasted_water)}")