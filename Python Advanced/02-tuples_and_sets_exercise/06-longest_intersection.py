n = int(input())
longest_intersection_set = set()

for _ in range(n):
    first_range_data, second_range_data = input().split('-')
    first_range_start = int(first_range_data.split(',')[0])
    first_range_end = int(first_range_data.split(',')[1])
    first_range_set = [int(el) for el in range(first_range_start, first_range_end + 1)]
    first_range_set = set(first_range_set)
    second_range_start = int(second_range_data.split(',')[0])
    second_range_end = int(second_range_data.split(',')[1])
    second_range_set = [int(el) for el in range(second_range_start, second_range_end + 1)]
    second_range_set = set(second_range_set)

    current_intersection = first_range_set.intersection(second_range_set)

    if len(longest_intersection_set) < len(current_intersection):
        longest_intersection_set = current_intersection

print(f"Longest intersection is [{', '.join([str(el) for el in longest_intersection_set])}] with length {len(longest_intersection_set)}")