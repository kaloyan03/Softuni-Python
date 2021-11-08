from collections import deque
from datetime import datetime, timedelta
data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
time = time + timedelta(seconds=1)

robots = {}
available_robots = deque()
products = deque()

for i in range(len(data)):
    robots_data = data[i].split("-")
    robot_name = robots_data[0]
    processing_time = int(robots_data[1])
    robots[robot_name] = {"processing time": processing_time, "available_at": time}
    available_robots.append(robot_name)


product = input()
while not product == 'End':
    products.append(product)
    product = input()

while len(products) > 0:
    curr_product = products.popleft()
    if available_robots:
        robot = available_robots.popleft()
        robots[robot]['available_at'] = time + timedelta(seconds=robots[robot]['processing time'])
        print(f"{robot} - {curr_product} [{time.strftime('%H:%M:%S')}]")

    else:
        products.append(curr_product)
        for r in robots:
            if robots[r]['available_at'] == time:
                available_robots.append(r)
                robots[r]['available_at'] = time + timedelta(seconds=robots[r]['processing time'])
                print(f"{r} - {curr_product} [{time.strftime('%H:%M:%S')}]")
                available_robots.popleft()
                products.pop()




    time = time + timedelta(seconds=1)