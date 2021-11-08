rows, cols = list(map(int, input().split()))
matrix = []
for row_index in range(rows):
    matrix.append([])
    for col_index in range(cols):
        matrix[row_index].append(0)



word = input()
word_index = 0
for row_index in range(rows):
    for col_index in range(cols):
        curr_char = word[word_index]
        matrix[row_index][col_index] = curr_char
        word_index += 1
        if word_index == len(word):
            word_index = 0

for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    for col_index in range(cols):
        print(''.join(matrix[row_index][col_index]), end='')
    print()