def print_res(result):
    sorted_res = sorted(result.items(), key= lambda kvp: kvp[0])
    for symbol, count in sorted_res:
        print(f"{symbol}: {count} time/s")

word = input()
symbols = {}
for char in word:
    symbols[char] = word.count(char)

print_res(symbols)