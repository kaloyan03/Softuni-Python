def filter_numbers(nums):
    positives = [el for el in nums if el > 0]
    negatives = [el for el in nums if el < 0]

    return positives,negatives


def get_numbers_sum(nums):
    the_sum = sum(nums)
    return the_sum


def print_result(first_sum, second_sum):
    print(second_sum)
    print(first_sum)
    if first_sum < abs(second_sum):
        print(f"The negatives are stronger than the positives")

    else:
        print(f"The positives are stronger than the negatives")


numbers = [int(el) for el in input().split()]
positive, negative = filter_numbers(numbers)
postive_sum = get_numbers_sum(positive)
negative_sum = get_numbers_sum(negative)
print_result(postive_sum, negative_sum)
