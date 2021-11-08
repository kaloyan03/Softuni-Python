clothes = list(map(int , input().split()))
rack_capacity = int(input())
racks = 1
sum_clothes = 0

while clothes:
    if sum_clothes + clothes[-1] <= rack_capacity:
        sum_clothes += clothes.pop()


    else:
        racks += 1
        sum_clothes = 0


print(racks)