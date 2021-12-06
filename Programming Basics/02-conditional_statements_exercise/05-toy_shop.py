vacation_price = float(input())

puzzle_price = 2.60
dolls_price = 3
bear_price = 4.10
minions_price = 8.20
truck_price = 2


puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

all_puzzles_price = puzzles_count * puzzle_price
all_dolls_price = dolls_count * dolls_price
all_bears_price = bears_count * bear_price
all_minions_price = minions_count * minions_price
all_trucks_price = trucks_count * truck_price

all_toys_price = all_puzzles_price + all_dolls_price + all_bears_price + all_minions_price + all_trucks_price

if (total_toys_count >= 50):
    discount = all_toys_price * 0.25
    price_discount = all_toys_price - discount
    price_rent = price_discount * 0.1
    final_price = price_discount - price_rent

else:
    final_price = all_toys_price - (all_toys_price * 0.1)

if final_price >= vacation_price:
    print(f"Yes! {abs(final_price - vacation_price):.2f} lv left.")
else:
    print(f"Not enough money! {abs(final_price - vacation_price):.2f} lv needed.")






