python
import pytest
from src.operations.subtraction import Subtraction

def test_subtraction_positive_integers():
    assert Subtraction.execute(5, 3) == 2

def test_subtraction_negative_integers():
    assert Subtraction.execute(-1, -1) == 0

def test_subtraction_zero():
    assert Subtraction.execute(0, 5) == -5
    assert Subtraction.execute(5, 0) == 5

def test_subtraction_decimal_numbers():
    assert Subtraction.execute(2.5, 1.0) == 1.5
    assert Subtraction.execute(-2.5, -1.0) == -1.5

def test_subtraction_large_numbers():
    assert Subtraction.execute(1e9, 5e8) == 5e8
    assert Subtraction.execute(1e-9, 5e-10) == 4.5e-10

def test_subtraction_non_numeric_inputs():
    with pytest.raises(TypeError):
        Subtraction.execute("5", 3)
    with pytest.raises(TypeError):
        Subtraction.execute(5, "3")
    with pytest.raises(TypeError):
        Subtraction.execute("5", "3")