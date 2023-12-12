import puzzles.day_4.day_4a as Day4a

class TestDay4a:
    def test_solve(self):
        # This requires a fixture
        result = Day4a.Day4a().solve()
        assert result == 23028
