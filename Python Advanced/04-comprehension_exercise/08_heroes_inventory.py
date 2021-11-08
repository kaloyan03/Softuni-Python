names = input().split(", ")

command_input = input()
inventory = {name: {} for name in names}
while not command_input == 'End':
    tokens = command_input.split("-")
    name = tokens[0]
    item = tokens[1]
    cost = int(tokens[2])
    if not inventory[name]:
        inventory[name] = {'items' : [], 'cost': []}
    if not item in inventory[name]['items']:
        inventory[name]['items'].append(item)
        inventory[name]['cost'].append(cost)

    command_input = input()

for key ,value in inventory.items():
    print(f"{key} -> Items: {len(value['items'])}, Cost: {(sum(value['cost']))}")