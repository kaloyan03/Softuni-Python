bad_grades_count = int(input())
total_grades = 0
counter = 0
name = input()

last_task_name = ''
grades_count = 0
while name != 'Enough':
    grade = int(input())
    total_grades += grade
    grades_count += 1
    if grade <= 4:
        counter += 1
    last_task_name = name
    if counter == bad_grades_count:
        break

    name = input()



if name == 'Enough':
    print(f"Average score: {total_grades / grades_count:.2f}\nNumber of problems: {grades_count}\nLast problem: {last_task_name}")
else:
    print(f'You need a break, {bad_grades_count} poor grades.')

