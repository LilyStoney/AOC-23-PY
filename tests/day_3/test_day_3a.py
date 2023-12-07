import puzzles.day_3.day_3a as Day3a

class TestDay3a:
    def test_solve(self):
        # This requires a fixture
        result = Day3a.Day3a().solve()
        assert result == 525181
