def get_min_number(nums):
    print(f"The minimum number is {min(nums)}")

def get_max_number(nums):
    print(f"The maximum number is {max(nums)}")

def get_sum_numbers(nums):
    print(f"The sum number is: {sum(nums)}")

numbers = [int(el) for el in input().split()]
get_min_number(numbers)
get_max_number(numbers)
get_sum_numbers(numbers)