import string
import re
import numpy

class Day2b:
    def __init__(self):
        with open("puzzles/day_2/inputs.txt", "r") as file:
            self.games = file.readlines()

    def solve(self):
        result = (sum(num for num in self.__cube_powers()))
        print(result)
        return(result)

    def __cube_powers(self):
        cube_powers = []

        for game in self.games:
            formatted_game = self.__format_game(game)
            cube_powers.append(self.__find_game_cube_power(formatted_game))

        return cube_powers

    def __format_game(self, game):
        split_game = game.translate(str.maketrans('', '', string.punctuation))
        split_game = re.sub('\n', '', split_game).split(' ')

        return [split_game[i:i + 2] for i in range(0, len(split_game), 2)]

    def __find_game_cube_power(self, game):
        game_summary = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for cube_value, colour in game:
            if colour in game_summary.keys():
                if int(cube_value) > game_summary[colour]:
                    game_summary[colour] = int(cube_value)

        return numpy.prod([*game_summary.values()])


Day2b().solve()
