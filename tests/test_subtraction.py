python
        import pytest
from src.operations.subtraction import Subtraction

class TestSubtraction:
    def setup_method(self):
        self.subtraction = Subtraction()

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("x, y, expected", [
        (1.0, 2.0, -1.0),
        (-1.0, -2.0, 1.0),
    ])
    def test_execute(self, x, y, expected):
        assert self.subtraction.execute(x, y) == expected