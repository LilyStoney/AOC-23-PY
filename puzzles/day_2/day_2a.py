import string
import re


class Day2a:
    MAX_CUBES = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def __init__(self, input_file="puzzles/day_2/inputs.txt"):
        with open("puzzles/day_2/inputs.txt", "r") as file:
            self.games = file.readlines()

    def solve(self):
        result = sum(self.__validate_game(self.__format_game(game)) for game in self.games)

        print(result)
        return(result)

    def __format_game(self, game):
        cleaned_game = game.translate(str.maketrans('', '', string.punctuation))
        cleaned_game = re.sub('\n', '', cleaned_game).split(' ')

        return [cleaned_game[i:i + 2] for i in range(0, len(cleaned_game), 2)]

    def __validate_game(self, game):
        id_value = game[0][1]
        round_validity = []

        for value, colour in game[1:]:
            if int(value) > self.MAX_CUBES[colour]:
                round_validity.append(False)
            else:
                round_validity.append(True)

        return int(id_value) if all(round_validity) else 0


Day2a().solve()
