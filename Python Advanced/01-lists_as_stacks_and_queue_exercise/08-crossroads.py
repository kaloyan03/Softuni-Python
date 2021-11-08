from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
command_input = input()
cars = deque()
cars_entered = 0
timer = 0
is_crashed = False
where_is_hit = ''
while not command_input == 'END':
    if command_input == 'green':
        if cars:
            car = cars.popleft()
            seconds_left = green_light_duration - len(car)
            while seconds_left > 0:
                cars_entered += 1
                if cars:
                    car = cars.popleft()
                    seconds_left -= len(car)
                else:
                    break

            if seconds_left == 0:
                cars_entered += 1
            if free_window_duration >= abs(seconds_left):
                if seconds_left < 0:
                    cars_entered += 1
            else:
                idx = free_window_duration + seconds_left
                print(f"A crash happened!")
                print(f"{car} was hit at {car[idx]}.")
                is_crashed = True
                break
    else:
        cars.append(command_input)


    command_input = input()

if not is_crashed:
    print(f"Everyone is safe.\n{cars_entered} total cars passed the crossroads.")








# from collections import deque
#
# green_light = int(input())
# window = int(input())
#
# cars = deque()
# cars_counter = 0
# crashed = False
#
# command = input()
# while command != "END":
#     if command == "green":
#         if cars:
#             current = cars.popleft()
#             seconds_left = green_light - len(current)
#             while seconds_left > 0:
#                 cars_counter += 1
#                 if cars:
#                     current = cars.popleft()
#                     seconds_left -= len(current)
#                 else:
#                     break
#             if seconds_left == 0:
#                 cars_counter += 1
#             if window >= abs(seconds_left):
#                 if seconds_left < 0:
#                     cars_counter += 1
#             else:
#                 idx = window + seconds_left
#                 print("A crash happened!")
#                 print(f"{current} was hit at {current[idx]}.")
#                 crashed = True
#                 break
#     else:
#         cars.append(command)
#     command = input()
#
# if not crashed:
#     print("Everyone is safe.")
#     print(f"{cars_counter} total cars passed the crossroads.")

