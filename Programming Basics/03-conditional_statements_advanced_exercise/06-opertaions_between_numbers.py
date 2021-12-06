num_1 = int(input())
num_2 = int(input())
operator = input()

if operator == '+' or operator == "-" or operator == "*":
    result = 0
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2

    if result % 2 == 0:
        print(f'{num_1} {operator} {num_2} = {result} - even')
    else:
        print(f'{num_1} {operator} {num_2} = {result} - odd')

#"{N1} {оператор} {N2} = {резултат} – {even/odd}
elif operator == '/':
    if num_2 == 0:
        print(f'Cannot divide {num_1} by zero')
    else:
        print(f"{num_1} / {num_2} = {num_1 / num_2:.2f}" )

elif operator == "%":
    if num_2 == 0:
        print(f'Cannot divide {num_1} by zero')
    else:
        print(f"{num_1} % {num_2} = {num_1 % num_2}")