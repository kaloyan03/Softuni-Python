searched_book = input()
book = input()
count = 0
while searched_book != book:
    if book == 'No More Books':
        break
    count += 1
    book = input()


if book == searched_book:
    print(f'You checked {count} books and found it.')
elif book == 'No More Books':
    print(f'The book you search is not here!\nYou checked {count} books.')