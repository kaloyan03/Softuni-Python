numbers = [int(x) for x in input().split(", ")]

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]
positive_numbers = [n for n in numbers if n >= 0]
negative_numbers = [n for n in numbers if n < 0]

print(f"Positive: {', '.join(str(x) for x in positive_numbers)}")
print(f"Negative: {', '.join(str(x) for x in negative_numbers)}")
print(f"Even: {', '.join(str(x) for x in even_numbers)}")
print(f"Odd: {', '.join(str(x) for x in odd_numbers)}")