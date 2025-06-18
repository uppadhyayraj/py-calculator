import pytest
from math import sqrt
from src.operations.squareroot import SquareRoot

class TestSquareRoot:
    def test_execute(self):
        # Positive cases
        for input in range(-10, 10):
            expected_output = sqrt(input) if input >= 0 else None
            assert SquareRoot.execute(input) == expected_output
        
        # Negative case: negative input
        with pytest.raises(ValueError):
            SquareRoot.execute(-10)