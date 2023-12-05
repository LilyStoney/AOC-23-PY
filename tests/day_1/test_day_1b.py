import puzzles.day_1.day_1b as Day1b

class TestDay1b:
    def test_solve(self):
        result = Day1b.Day1b().solve()
        assert result == 54985

    def test_match_string(self):
        result = Day1b.Day1b()._Day1b__match_string('1abc2')
        assert result == ['1', '2']

    def test_match_string_with_words(self):
        result = Day1b.Day1b()._Day1b__match_string('1two3')
        assert result == ['1', '3']

    def test_match_string_one_number(self):
        result = Day1b.Day1b()._Day1b__match_string('1twothree')
        assert result == ['1', 'three']

    def test_match_string_shared_letter(self):
        result = Day1b.Day1b()._Day1b__match_string('eightwothree')
        assert result == ['eight', 'three']

    def test_match_string_shared_letter_at_end(self):
        result = Day1b.Day1b()._Day1b__match_string('threeeightwo')
        assert result == ['three', 'two']
