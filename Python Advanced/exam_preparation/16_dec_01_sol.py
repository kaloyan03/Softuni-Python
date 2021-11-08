from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

total_matches = 0

while True:
    if len(males) <= 0:
        break

    elif len(females) <= 0:
        break

    current_female = females.popleft()
    current_male = males[-1]

    if current_male <= 0:
        males.pop()
        females.appendleft(current_female)
        continue

    elif current_female <= 0:
        continue

    if current_male % 25 == 0:
        for _ in range(2):
            if males:
                males.pop()
            else:
                break
        continue

    elif current_female % 25 == 0:
        for _ in range(2):
            if females:
                females.popleft()
            else:
                break

        continue


    if current_female == current_male:
        males.pop()
        total_matches += 1
    else:

        current_male -= 2
        males.pop()
        males.append(current_male)

print(f"Matches: {total_matches}")

print(f"Males left:", end= ' ')
if len(males) > 0:
    print(f"{', '.join([str(el) for el in reversed(males)])}")
else:
    print('none')
print(f"Females left:", end=' ')
if len(females) > 0:
    print(f"{', '.join([str(el) for el in females])}")
else:
    print('none')

