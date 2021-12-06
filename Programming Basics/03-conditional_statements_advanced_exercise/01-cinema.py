ticket_type = input()
rows = int(input())
cols = int(input())

price = 0
if ticket_type == 'Premiere':
    price = 12.00
elif ticket_type == 'Normal':
    price = 7.50
elif ticket_type == 'Discount':
    price = 5.00

income = rows * cols * price
print(f"{income:.2f} leva")