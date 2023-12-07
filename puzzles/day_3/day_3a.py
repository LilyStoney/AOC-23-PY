import re

class Day3a:
    def __init__(self, input_file="puzzles/day_3/inputs.txt"):
        with open(input_file, "r") as file:
            self.schematic = file.readlines()

    def solve(self):
        result = (sum(self.__calculate_parts()))
        print(result)
        return(result)

    def __calculate_parts(self):
        parts = []

        for idx, line in enumerate(self.schematic):
            for match in re.finditer(r"\d+", line):
                char_range = self.__format_match(match)
                row_range  = self.__row_range(idx)
                characters = [self.schematic[row_index].rstrip()[char_position] for row_index in row_range for char_position in char_range]

                for char in characters:
                    if re.match(r"[^a-zA-Z0-9.]", char):
                        parts.append(int(match[0]))
                    else:
                        parts.append(0)

        return(parts)


    def __format_match(self, match):
        start  = max(match.start() - 1, 0)
        finish = min(match.end(), 139)

        return list(range(start, finish + 1))

    def __row_range(self, idx):
        starting_row = max(idx - 1, 0)
        ending_row   = min(idx + 1, 139)

        return list(range(starting_row, ending_row + 1))


Day3a().solve()
