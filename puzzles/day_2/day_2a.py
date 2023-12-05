import string
import re

class Day2a:
    MAX_CUBES = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def __init__(self):
        with open("puzzles/day_2/inputs.txt", "r") as file:
            self.games = file.readlines()

    def solve(self):
        result = (sum(num for num in self.__valid_games()))
        print(result)
        return(result)

    def __valid_games(self):
        valid_games = []

        for game in self.games:
            formatted_game = self.__format_game(game)
            valid_games.append(self.__validate_games(formatted_game))

        return valid_games

    def __format_game(self, game):
        split_game = game.translate(str.maketrans('', '', string.punctuation))
        split_game = re.sub('\n', '', split_game).split(' ')

        return [split_game[i:i + 2] for i in range(0, len(split_game), 2)]

    def __validate_games(self, game):
        game_summary = {
            "id": None,
            "round_validity": []
        }

        for chunk in game:
            if chunk[1] in self.MAX_CUBES.keys():
                if int(chunk[0]) > self.MAX_CUBES[chunk[1]]:
                    game_summary["round_validity"].append(False)
                else:
                    game_summary["round_validity"].append(True)
            else:
                game_summary["id"] = (chunk[1])

        if all(game_summary["round_validity"]):
            return int(game_summary["id"])
        else:
            return 0


Day2a().solve()
