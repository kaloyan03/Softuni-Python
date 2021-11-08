def check_if_even(length):
    if length % 2 == 0:
        return True
    return False
text = input().split()
result = [word for word in text if check_if_even(len(word))]
for word in result:
    print(word)



# result = []
# for word in text:
#     length = len(word)
#     if length % 2 == 0:
#         result.append(word)
#
# for word in result:
#     print(word)