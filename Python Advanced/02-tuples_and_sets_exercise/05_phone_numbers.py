command = input()
data = []
while not command.isdigit():
    data.append(command)

    command = input()

peoples = {}

for el in data:
    name, number = el.split("-")
    peoples[name] = number
searched_peoples = []
n = int(command)
for _ in range(n):
    searched_peoples.append(input())

for el in searched_peoples:
    if el in peoples:
        print(f"{el} -> {peoples[el]}")

    else:
        print(f"Contact {el} does not exist.")