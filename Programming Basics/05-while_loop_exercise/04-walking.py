target = 10000

total_steps = 0

while total_steps < target:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        total_steps += steps
        break
    total_steps += int(steps)

diff = abs(target - total_steps)

if total_steps >= target:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

else:
    print(f'{diff} more steps to reach goal.')