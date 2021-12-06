budget = float(input())
season = input()
destination = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price += budget * 0.30
    elif season == 'winter':
        price += budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price += budget * 0.40
    elif season == 'winter':
        price += budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    if season == 'winter' or season == 'summer':
        price += budget * 0.90

print(f'Somewhere in {destination}')
if season == 'winter' or destination == 'Europe':
    print(f"Hotel - {price:.2f}")
elif season == 'summer':
    print(f"Camp - {price:.2f}")
