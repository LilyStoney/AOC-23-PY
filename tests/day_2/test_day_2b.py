import puzzles.day_2.day_2b as Day2b

class TestDay2b:
    def test_solve(self):
        # This requires a fixture
        result = Day2b.Day2b().solve()
        assert result == 56322

    def test_cube_powers(self):
        # This requires a fixture
        # result = Day2b.Day2b()._Day2b__cube_powers()
        # assert result == []
        pass

    def test_format_game(self):
        result = Day2b.Day2b()._Day2b__format_game('Game 1: 5 red, 6 green, 7 blue; 4 green, 3 blue; 2 red')
        assert result == [
            ['Game', '1'],
            ['5', 'red'],
            ['6', 'green'],
            ['7', 'blue'],
            ['4', 'green'],
            ['3', 'blue'],
            ['2', 'red']
        ]

    def test_find_game_cube_power(self):
        result = Day2b.Day2b()._Day2b__find_game_cube_power([
            ['Game', '1'],
            ['5', 'red'],
            ['6', 'green'],
            ['7', 'blue'],
            ['4', 'green'],
            ['3', 'blue'],
            ['2', 'red']
        ])
        assert result == 210
