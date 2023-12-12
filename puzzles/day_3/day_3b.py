import re
from collections import defaultdict
from functools import reduce
from operator import mul

class Day3b:
    def __init__(self, input_file="puzzles/day_3/inputs.txt"):
        with open(input_file, "r") as file:
            self.schematic = file.readlines()

    def solve(self):
        result = (sum(self.__calculate_parts()))
        print(result)
        return(result)

    def __calculate_parts(self):
        gears = defaultdict(list)

        for idx, line in enumerate(self.schematic):
            for number_match in re.finditer(r"\d+", line):
                char_range = self.__format_match(number_match)
                row_range  = self.__row_range(idx)

                for row_index in row_range:
                    for asterisk_position in re.finditer(r"\*", self.schematic[row_index].rstrip()):
                        gear_position = asterisk_position.start()

                        if (gear_position >= char_range[0]) and (gear_position <= char_range[-1]):
                            gears[row_index, gear_position].append(int(number_match[0]))

        gears_with_two_parts = [value for _, value in gears.items() if len(value) == 2]

        return [reduce(mul, gear_parts) for gear_parts in gears_with_two_parts]

    def __format_match(self, match):
        start  = max(match.start() - 1, 0)
        finish = min(match.end(), 139)

        return list(range(start, finish + 1))

    def __row_range(self, idx):
        starting_row = max(idx - 1, 0)
        ending_row   = min(idx + 1, 139)

        return list(range(starting_row, ending_row + 1))


Day3b().solve()
