#спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече
#	Градусите - цяло число;
#	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
# 10 <= градуси <= 18     18 < градуси <= 24       градуси >= 25
degree = int(input())
time = input()
outfit = str
shoes = str
if time == 'Morning':
    if 10 <= degree <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time == 'Afternoon':
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degree <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degree >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif time == 'Evening':
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

else:
    print()

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
