needed_money = float(input())
available_money = float(input())
count = 0
total_days = 0

while available_money < needed_money:
    action = input()
    amount = float(input())
    total_days += 1
    if action == 'save':
        available_money += amount
        count = 0
    else:
        count += 1
        if available_money - amount < 0:
            available_money = 0
        else:
            available_money -= amount

        if count == 5:
            break

if needed_money <= available_money:
    print(f'You saved the money for {total_days} days.')
elif count == 5:
    print(f"You can't save the money.")
    print(f"{total_days}")