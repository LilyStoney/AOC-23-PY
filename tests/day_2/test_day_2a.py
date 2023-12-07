import puzzles.day_2.day_2a as Day2a

class TestDay2a:
    def test_solve(self):
        # This requires a fixture
        result = Day2a.Day2a().solve()
        assert result == 2447

    def test_format_game(self):
        result = Day2a.Day2a()._Day2a__format_game('Game 1: 5 red, 6 green, 7 blue; 4 green, 3 blue; 2 red')
        assert result == [
            ['Game', '1'],
            ['5', 'red'],
            ['6', 'green'],
            ['7', 'blue'],
            ['4', 'green'],
            ['3', 'blue'],
            ['2', 'red']
        ]

    def test_validate_game(self):
        result = Day2a.Day2a()._Day2a__validate_game([
            ['Game', '1'],
            ['5', 'red'],
            ['6', 'green'],
            ['7', 'blue'],
            ['4', 'green'],
            ['3', 'blue'],
            ['2', 'red']
        ])

        assert result == 1

    def test_validate_impossible_game(self):
        result = Day2a.Day2a()._Day2a__validate_game([
            ['Game', '1'],
            ['5', 'red'],
            ['30', 'green'],
            ['7', 'blue'],
            ['4', 'green'],
            ['3', 'blue'],
            ['2', 'red']
        ])

        assert result == 0
