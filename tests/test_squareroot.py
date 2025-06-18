python
import pytest
from src.operations.squareroot import SquareRoot

class TestSquareRoot:
    def test_negative_input(self):
        with pytest.raises(ValueError) as exc_info:
            SquareRoot.execute(-1.0)
        assert str(exc_info.value) == "Cannot calculate square root of a negative number"

    def test_zero_input(self):
        result = SquareRoot.execute(0.0)
        assert result == 0.0

    def test_positive_input(self):
        result = SquareRoot.execute(4.0)
        assert result == 2.0