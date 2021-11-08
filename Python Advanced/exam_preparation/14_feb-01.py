from collections import deque

def read_input(is_test=False):
    if is_test:
        f_e = deque([5, 6, 4, 16, 11, 5, 30, 2, 3, 27])
        e_p = [1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22]
        return f_e, e_p
    else:
        f_e = deque([int(x) for x in input().split(', ')])
        e_p = [int(x) for x in input().split(', ')]
        return f_e, e_p


def print_result(successful, f_e, e_p, palm ,willow, crossette):
    if successful:
        print(f"Congrats! You made the perfect firework show!")


    else:
        print(f"Sorry. You can't make the perfect firework show.")


    if f_e:
        print(f"Firework Effects left: {', '.join([str(el) for el in f_e])}")
    if e_p:
        print(f"Explosive Power left: {', '.join([str(el) for el in e_p])}")
    print(f"Palm Fireworks: {palm}")
    print(f"Willow Fireworks: {willow}")
    print(f"Crossette Fireworks: {crossette}")

def check_fireworks_count(palm, willow, crossette):
    if palm >= 3 and willow >= 3 and crossette >= 3:
        return True
    return False



firework_effects, explosive_power = read_input(is_test=False)
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0


while True:
    if check_fireworks_count(palm_fireworks, willow_fireworks, crossette_fireworks):
        print_result(True, firework_effects, explosive_power, palm_fireworks, willow_fireworks, crossette_fireworks)
        break
    if len(firework_effects) == 0 or len(explosive_power) == 0:
        print_result(False, firework_effects, explosive_power, palm_fireworks, willow_fireworks, crossette_fireworks)
        break
    current_firework_effect = firework_effects.popleft()
    current_explosive_power = explosive_power.pop()


    if current_firework_effect <= 0:
        explosive_power.append(current_explosive_power)
        continue
    elif current_explosive_power <= 0:
        firework_effects.appendleft(current_firework_effect)
        continue

    mixed_fireworks = current_firework_effect + current_explosive_power

    if mixed_fireworks % 3 == 0 and not mixed_fireworks % 5 == 0:
        palm_fireworks += 1


    elif mixed_fireworks % 5 == 0 and not mixed_fireworks % 3 == 0:
        willow_fireworks += 1

    elif mixed_fireworks % 5 == 0 and mixed_fireworks % 3 == 0:
        crossette_fireworks += 1

    else:
        current_firework_effect -= 1
        firework_effects.append(current_firework_effect)
        explosive_power.append(current_explosive_power)







