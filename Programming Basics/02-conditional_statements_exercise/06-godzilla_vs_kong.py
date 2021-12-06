film_budget = float(input())
statists_count = int(input())
cloth_price = float(input())

film_decor = film_budget - (film_budget * 0.9)

if statists_count > 150:
    clothes_price_for_statists = cloth_price * statists_count - (cloth_price * statists_count * 0.1)
else:
    clothes_price_for_statists = cloth_price * statists_count

film_price = film_decor + clothes_price_for_statists

if film_price > film_budget:
    print(f'Not enough money!\nWingard needs {abs(film_price - film_budget):.2f} leva more.')
else:
    print(f'Action!\nWingard starts filming with {abs(film_price - film_budget):.2f} leva left.')