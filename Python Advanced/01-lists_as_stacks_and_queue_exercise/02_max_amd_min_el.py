n = int(input())
s = []
for _ in range(n):
    sequence = input()
    if sequence.startswith("1"):
        data = sequence.split()
        element = int(data[1])
        s.append(element)

    else:
        number = int(sequence)
        if number == 2:
            if s:
                s.pop()
        elif number == 3:
            if s:
                print(max(s))

        elif number == 4:
            if s:
                print(min(s))

s = reversed(s)
print(', '.join([str(el) for el in s]))












# n = int(input())
#
# stack = []
#
# for iteration in range(1 , n + 1):
#     command = input().split()
#     query = int(command[0])
#     max_el = 0
#     min_el = 0
#     if query == 1:
#         element = int(command[1])
#         stack.append(element)
#
#     elif query == 2:
#         if not len(stack) == 0:
#             stack.pop()
#
#     elif query == 3:
#         print(max(stack))
#
#     elif query == 4:
#         print(min(stack))
#
#
# stack = reversed(stack)
# print(f"{', '.join([str(el) for el in stack])}")
#
