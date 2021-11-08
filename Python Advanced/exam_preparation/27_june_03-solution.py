def add_numbers_at_end(nums, line):
    line.extend(nums)
    return line

def add_numbers_at_beginning(nums,line):
    return f"{[*nums] + line}"

def list_manipulator(*args):
    line = args[0]
    second_parameter = args[1]
    third_parameter = args[2]
    numbers = []
    if len(args) > 3:
        numbers = args[3:]

    if second_parameter == 'add' and third_parameter == 'beginning':
        line = add_numbers_at_beginning(numbers, line)

    elif second_parameter == 'add' and third_parameter == 'end':
        line = add_numbers_at_end(numbers,line)

    elif second_parameter =='remove' and third_parameter == 'beginning':
        if numbers:
            line = line[numbers[0]:]
        else:
            line = line[1:]

    elif second_parameter == 'remove' and third_parameter == 'end':
        if numbers:
            line = line[:-numbers[0]]
        else:
            line = line[:-1]
    return line



import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(list_manipulator([1,2,3], "remove", "end"), [1, 2])
        self.assertEqual(list_manipulator([1,2,3], "remove", "beginning"), [2, 3])
        self.assertEqual(list_manipulator([1,2,3], "add", "beginning", 20), [20, 1, 2, 3])
        self.assertEqual(list_manipulator([1,2,3], "add", "end", 30), [1, 2, 3, 30])
        self.assertEqual(list_manipulator([1,2,3], "remove", "end", 2), [1])
        self.assertEqual(list_manipulator([1,2,3], "remove", "beginning", 2), [3])
        self.assertEqual(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40), [20, 30, 40, 1, 2, 3])
        self.assertEqual(list_manipulator([1,2,3], "add", "end", 30, 40, 50), [1, 2, 3, 30, 40, 50])

if __name__ == "__main__":
    unittest.main()