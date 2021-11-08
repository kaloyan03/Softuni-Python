def kwargs_length(**kwargs):
    result = 0
    for el in kwargs:
        result += 1

    return result
dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
