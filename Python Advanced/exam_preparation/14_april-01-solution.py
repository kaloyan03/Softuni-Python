from collections import deque

def check_if_run_out(length):
    if length <= 0:
        return True
    return False

def print_result(is_completed, *args):
    if is_completed:
        print(f"All orders are successfully completed!\nTotal pizzas made: {args[0]}")
        print(f"Employees: {', '.join([str(el) for el in args[1]])}")
    else:
        print(f"Not all orders are completed.")
        print(f"Orders left: {', '.join([str(el) for el in args[0]])}")
def check_index_order(num):
    if 0 < num <= 10:
        return False
    return True
total_pizzas_made = 0
orders = deque([int(el) for el in input().split(", ")])
employees = [int(el) for el in input().split(", ")]
is_completed = False
stop_program = False

while True:
    if check_if_run_out(len(orders)):
        is_completed = True
        print_result(is_completed, total_pizzas_made, employees)
        break

    if check_if_run_out(len(employees)):
        print_result(is_completed, orders)
        break

    current_order = orders[0]
    current_emloyee = employees[-1]


    if check_index_order(current_order):
        orders.popleft()
        continue


    if current_order <= current_emloyee:
        total_pizzas_made += current_order
        employees.pop()
        orders.popleft()



    elif current_order > current_emloyee:
        order = current_order
        while current_order > 0:
            current_order -= current_emloyee
            employees.pop()
            if len(employees) > 0:
                current_emloyee = employees[-1]
            else:
                stop_program = True
                orders.popleft()
                orders.appendleft(current_order)
                print_result(is_completed, orders)
                break
        if stop_program:
            break
        orders.popleft()
        total_pizzas_made += order




