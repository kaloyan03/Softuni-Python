rows, columns = [int(el) for el in input().split()]
word = input()
snake = []
reached_max_rows = False
counter = 0
for rows_count in range(rows):

    if rows_count == 0:
        snake.append([])
    for char in word:
            snake[rows_count].append(char)
            counter += 1
            if rows_count == rows:
                reached_max_rows = True
                break

            if counter == columns:
                rows_count += 1
                snake.append([])
                counter = 0

    if reached_max_rows:
        break

a = 5