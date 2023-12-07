import string
import re
import numpy as np

class Day2b:
    def __init__(self, input_file="puzzles/day_2/inputs.txt"):
        with open(input_file, "r") as file:
            self.games = file.readlines()

    def solve(self):
        result = sum(self.__find_game_cube_power(self.__format_game(game)) for game in self.games)
        print(result)
        return(result)

    def __format_game(self, game):
        cleaned_game = game.translate(str.maketrans('', '', string.punctuation))
        cleaned_game = re.sub('\n', '', cleaned_game).split(' ')

        return [cleaned_game[i:i + 2] for i in range(0, len(cleaned_game), 2)]

    def __find_game_cube_power(self, game):
        game_summary = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for cube_value, colour in game[1:]:
            game_summary[colour] = max(game_summary[colour], int(cube_value))

        return np.prod([*game_summary.values()])


Day2b().solve()
