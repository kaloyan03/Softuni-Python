n = int(input())
salary = int(input())
deduction = 0

for i in range(n):
    website = input()
    if website == 'Facebook':
        deduction += 150
    elif website == 'Instagram':
        deduction += 100
    elif website == 'Reddit':
        deduction += 50
total_salary = salary - deduction
if total_salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{total_salary}')
