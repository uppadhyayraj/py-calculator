import pytest
from src.operations.subtraction import Subtraction

# Test cases for subtraction operation
def test_subtracting_two_positive_numbers():
    assert Subtraction.execute(10.0, 5.0) == 5.0

def test_subtracting_a_positive_number_from_a_negative_number():
    assert Subtraction.execute(-3.0, 2.0) == -5.0

def test_subtracting_zero_from_any_number():
    assert Subtraction.execute(7.0, 0.0) == 7.0

def test_subtracting_a_negative_number_from_a_positive_number():
    assert Subtraction.execute(4.0, -2.0) == 6.0

# Edge cases for subtraction operation
@pytest.mark.parametrize("x, y, expected", [
    (5.0, 3.0, 2.0),
    (-1.0, -2.0, 1.0),
    (0.0, 0.0, 0.0),
    (100.0, 50.0, 50.0)
])
def test_subtraction_edge_cases(x, y, expected):
    assert Subtraction.execute(x, y) == expected