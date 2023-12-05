import puzzles.day_1.day_1a as Day1a

class TestDay1a:
    def test_solve(self):
        result = Day1a.Day1a().solve()
        assert result == 55130

    def test_match_string(self):
        result = Day1a.Day1a()._Day1a__match_string('1abc2')
        assert result == ['1', '2']

    def test_match_string_with_words(self):
        result = Day1a.Day1a()._Day1a__match_string('1two3')
        assert result == ['1', '3']

    def test_match_string_one_number(self):
        result = Day1a.Day1a()._Day1a__match_string('1twothree')
        assert result == ['1', '1']
