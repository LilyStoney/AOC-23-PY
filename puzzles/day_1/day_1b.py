import re

class Day1b:
    NUMBERS = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    def __init__(self):
        with open("puzzles/day_1/inputs.txt", "r") as file:
            self.strings = file.readlines()

    def solve(self):
        result = sum(int(num) for num in self.__gather_numbers())
        print(result)
        return(result)

    def __gather_numbers(self):
        result_list = []

        for string in self.strings:
            numbers = self.__match_string(string)

            for num in numbers:
                if num in self.NUMBERS.keys():
                    numbers[numbers.index(num)] = str(self.NUMBERS[num])

            result_list.append(''.join(numbers))

        return result_list

    def __match_string(self, string):
        number_words = '|'.join(self.NUMBERS.keys())
        pattern = f'(?=(\d|{number_words}))'
        matches = re.findall(pattern, string)

        return [matches[0], matches[-1]] if matches else []


Day1b().solve()
