
#Read by console >>>><<<
#Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
#	Брой цветя - цяло число;
#	Бюджет - цяло число.


# DISCOUNTS >>>>>>>>>>>>><<<<<<<<<<<<<<<<<
#	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
#	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
#	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
#	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
#	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
#DISCOUNTS>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<

flower_type = input()
flower_num = int(input())
budget = int(input())
price = 0

if flower_type == 'Roses':
    price = 5
    if flower_num > 80:
        price -= price * 0.10 # price = price - price * 0.10




elif flower_type == 'Dahlias':
    price = 3.80
    if flower_num > 90:
        price -= price * 0.15

elif flower_type == 'Tulips':
    price = 2.80
    if flower_num > 80:
        price -= price * 0.15

elif flower_type == 'Narcissus':
    price = 3
    if flower_num < 120:
        price += price * 0.15

elif flower_type == 'Gladiolus':
    price = 2.50
    if flower_num < 80:
        price += price * 0.20

money_needed = flower_num * price
diff = abs(budget - money_needed) #absolute result
if budget >= money_needed:
    print(f'Hey, you have a great garden with {flower_num} {flower_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')

