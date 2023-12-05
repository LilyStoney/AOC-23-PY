import re

class Day1a:
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

            result_list.append(''.join(numbers))

        return result_list

    def __match_string(self, string):
        pattern = r'(\d)|\d(?!\d)'
        matches = re.findall(pattern, string)

        return [matches[0], matches[-1]] if matches else []


Day1a().solve()
