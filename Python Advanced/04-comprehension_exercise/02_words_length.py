words = input().split(', ')
result = {word: len(word) for word in words}
counter = 0
for key,value in result.items():
    counter += 1
    if counter == len(result):
        print(f"{key} -> {value}", end=" ")
        break
    print(f"{key} -> {value}", end=", ")





# for word in words:
#     result[word] = len(word)
# counter = 0
# for key,value in result.items():
#     counter += 1
#     if counter == len(result):
#         print(f"{key} -> {value}", end=" ")
#         break
#     print(f"{key} -> {value}", end=", ")
