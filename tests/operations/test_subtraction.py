import pytest
from src.operations.subtraction import Subtraction

def test_subtraction():
    assert Subtraction.execute(5, 3) == 2
    assert Subtraction.execute(1, 1) == 0
    assert Subtraction.execute(0, 5) == -5
    assert Subtraction.execute(2.5, 1.0) == 1.5
