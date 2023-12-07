import re

class Day3a:
    def __init__(self, input_file="puzzles/day_3/inputs.txt"):
        with open(input_file, "r") as file:
            self.schematic = file.readlines()

    def solve(self):
        result = (sum(num for num in self.__calculate_parts()))
        print(result)
        return(result)

    def __calculate_parts(self):
        parts = []

        for idx, line in enumerate(self.schematic):
            for match in re.finditer(r"\d+", line):
                char_range = self.__format_match(match)
                row_range  = self.__row_range(idx)
                characters = []

                for row in row_range:
                    line = re.sub('\n', '', self.schematic[row])

                    for num in char_range:
                        if num == 140:
                            continue
                        else:
                            characters.append(line[num])

                for char in characters:
                    if re.match(r"[^a-zA-Z0-9.]", char):
                        parts.append(int(match[0]))
                    else:
                        parts.append(0)

        return(parts)


    def __format_match(self, match):
        start      = match.start() - 1
        finish     = match.end()
        char_range = range(start, finish)

        return(char_range)

    def __row_range(self, idx):
        if idx > 0:
            starting_row = (idx - 1)
        else:
            starting_row = (idx)

        if idx == 140:
            ending_row = idx
        else:
            ending_row = (idx + 1)

        row_range = range(starting_row, ending_row)

        return(row_range)


Day3a().solve()
