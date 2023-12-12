import re
from collections import Counter
from functools import reduce

class Day4a:
    def __init__(self, input_file="puzzles/day_4/inputs.txt"):
        with open(input_file, "r") as file:
            self.schematic = file.readlines()

    def solve(self):
        result = sum(self.__calculate_points())
        print(result)
        return(result)

    def __calculate_points(self):
        total_points = []
        game_matches = {}

        for line in self.schematic:
            card_numbers = [int(num) for num in re.findall(r"\d+", line)]
            game_id = card_numbers[0]
            game_matches[game_id] = len([num for num, count in Counter(card_numbers[1:]).items() if count == 2])

        for game_id, matches in game_matches.items():
            if matches > 0:
                points = reduce(lambda acc, _: acc * 2, range(1, matches), 1)
                total_points.append(points)

        return total_points

Day4a().solve()
