from collections import deque

bracket = list(input())
bracket_as_queue = deque(bracket)
length = len(bracket)
mid_length = len(bracket) // 2


elements_left = deque()
elements_right = deque()

while True:
    if len(bracket) == mid_length:

        break

    else:
        elements_right.appendleft(bracket.pop())
while True:
    if len(bracket_as_queue) == mid_length:

        break

    else:
        elements_left.appendleft(bracket_as_queue.popleft())
elements_length = len(elements_right)
counter = 0
for big in elements_left:
    opposite = ''
    for small in elements_right:

        if big == '(':
            opposite = ')'
            if small == opposite:
                counter += 1
                elements_right.popleft()
                break

            elements_right.popleft()
            break
        elif big == '{':
            opposite = '}'
            if small == opposite:
                counter += 1
                break

            elements_right.popleft()
            break
        elif big == '[':
            opposite = ']'
            if small == opposite:
                counter += 1
                elements_right.popleft()
                break
            elements_right.popleft()
            break





if elements_length == counter:
    print(f"YES")
else:
    print("NO")