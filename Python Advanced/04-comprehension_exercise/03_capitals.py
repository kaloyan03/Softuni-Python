countries = input().split(', ')
capital_cities = input().split(", ")
result = {countries[index]:capital_cities[index] for index in range(len(countries))}
print(*[f"{key} -> {value}" for key, value in result.items()], sep="\n")