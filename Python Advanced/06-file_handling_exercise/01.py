from collections import deque
special_characters = ['-', ',', '.', '!', '?']
swap_character = "@"
even_lines = []
i = 0
with open("text.txt") as file:
    for line in file.readlines():
        if i % 2 == 0:
            even_lines.append(line[:-1])
        i += 1



for line in even_lines:
    for char in special_characters:
        if char in line:
            line = line.replace(char, swap_character)
    words =line.split()
    reversed_order = deque()
    for word in words:
        reversed_order.appendleft(word)
    print(' '.join(reversed_order))