import pytest
from src.operations.squareroot import SquareRoot
from math import sqrt

def test_calculate_positive_square_root():
    assert SquareRoot.execute(9) == 3

def test_handle_negative_input():
    with pytest.raises(ValueError):
        SquareRoot.execute(-1)

def test_zero_input():
    assert SquareRoot.execute(0) == 0

def test_perfect_square_input():
    assert SquareRoot.execute(16) == 4

def test_negative_number_raises_valueerror():
    with pytest.raises(ValueError):
        SquareRoot.execute(-1)