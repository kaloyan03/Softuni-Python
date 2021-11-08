from string import punctuation

def count_letters(string):
    counter = 0
    for char in string:
        if char.isalpha():
            counter += 1

    return counter


def count_punctuations(string, symbols):
    occurrences = 0
    for symbol in symbols:
        if symbol in string:
            occurrences += string.count(symbol)
    return occurrences
punctuation_symbols = punctuation
counter = 1
with open('text.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1]
        letters_count = count_letters(line)
        punctuation_occurrences = count_punctuations(line, punctuation_symbols)



        print(f"Line {counter}: {line} ({letters_count})({punctuation_occurrences})")
        counter += 1