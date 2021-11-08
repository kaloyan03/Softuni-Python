n = int(input())
names = []
for _ in range(n):
    names.append(input())

names = set(names)

for name in names:
    print(name)







# def input_to_list(count):
#     lines = []
#     for _ in range(count):
#         lines.append(input())
#
#     return lines
#
#
# def print_result(res):
#     res = set(res)
#     for el in res:
#         print(el)
#
#
# n = int(input())
#
# data = input_to_list(n)
# print_result(data)

