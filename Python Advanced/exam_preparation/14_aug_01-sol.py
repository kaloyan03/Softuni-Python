from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]

total_time = 0
ran_out_of_taxis = False
while len(customers) > 0:
    if len(taxis) <= 0:
        print(f"Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join([str(x) for x in customers])}")
        ran_out_of_taxis = True
        break
    current_customer = customers[0]
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()



if not ran_out_of_taxis:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")