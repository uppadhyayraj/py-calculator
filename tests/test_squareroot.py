python
import pytest
from src.operations.squareroot import SquareRoot

def test_execute_negative_input():
    with pytest.raises(ValueError):
        SquareRoot.execute(-1.0)

def test_execute_zero_input():
    assert SquareRoot.execute(0.0) == 0.0

def test_execute_positive_integer_input():
    assert SquareRoot.execute(4.0) == 2.0

def test_execute_positive_floating_point_input():
    assert pytest.approx(SquareRoot.execute(2.5), rel_tol=1e-9) == 1.5811388300841898