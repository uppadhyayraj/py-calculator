import pytest
from src.operations.multiplication import Multiplication

def test_multiplication():
    assert Multiplication.execute(2, 3) == 6
    assert Multiplication.execute(-2, 3) == -6
    assert Multiplication.execute(0, 5) == 0
    assert Multiplication.execute(2.5, 2) == 5.0
