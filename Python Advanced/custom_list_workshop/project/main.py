import sys
from copy import deepcopy


class CustomList():
    def __init__(self):
        self.data = []

    def append(self, value):
        return self.data.append(value)

    def remove(self, index):
        return self.data.pop(index)

    def get(self, index):
        return self.data[index]

    def extend(self, iterable):
        return self.data.extend(iterable)

    def insert(self, index, value):
        self.data.insert(index, value)
        return self.data

    def pop(self):
        return self.data.pop()

    def clear(self):
        self.data.clear()

    def index(self, value):
        return self.data.index(value)

    def count(self, value):
        return self.data.count(value)

    def reverse(self):
        return self.data.reverse()

    def copy(self):
        return deepcopy(self.data)

    def size(self):
        return len(self.data)

    def dictionize(self):
        dict_from_list = {}

        for i in range(0, len(self.data), 2):
            try:
                dict_from_list[self.data[i]] = self.data[i + 1]
            except IndexError:
                dict_from_list[self.data[i]] = ' '

        return dict_from_list

    def move(self, amount):
        values = self.data[:amount]

        for value in values:
            self.data.remove(value)

        self.data.extend(values)

        return self.data

    def sum(self):
        total_sum = 0

        for value in self.data:
            if isinstance(value, str):
                value_length = len(value)
                total_sum += value_length

            elif isinstance(value, int):
                total_sum += value

        return total_sum


    def overbound(self):
        current_biggest = -sys.maxsize

        for value in self.data:
            if isinstance(value, str):
                value_length = len(value)
                if value_length > current_biggest:
                    current_biggest = value_length

            elif isinstance(value, int):
                if value > current_biggest:
                    current_biggest = value

        return current_biggest


    def underbound(self):
        current_smallest = sys.maxsize

        for value in self.data:
            if isinstance(value, str):
                value_length = len(value)
                if value_length < current_smallest:
                    current_smallest = value_length

            elif isinstance(value, int):
                if value < current_smallest:
                    current_smallest = value

        return current_smallest

