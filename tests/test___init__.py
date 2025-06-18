# tests/test_operations.py
import pytest
from src.operations import *

def test_addition():
    add = Addition()
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    with pytest.raises(ValueError):
        add(float('inf'), float('inf'))

def test_subtraction():
    sub = Subtraction()
    assert sub(5, 3) == 2
    assert sub(-1, -2) == 1
    assert sub(0, 0) == 0
    with pytest.raises(ValueError):
        sub(float('inf'), float('inf'))

def test_multiplication():
    mul = Multiplication()
    assert mul(2, 3) == 6
    assert mul(-1, -2) == 2
    assert mul(0, 5) == 0
    with pytest.raises(ValueError):
        mul(float('inf'), float('inf'))

def test_division():
    div = Division()
    assert div(6, 3) == 2
    assert div(-4, -2) == 2
    assert div(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
    with pytest.raises(ValueError):
        div(float('inf'), float('inf'))

def test_square():
    sq = Square()
    assert sq(2) == 4
    assert sq(-3) == 9
    assert sq(0) == 0
    with pytest.raises(ValueError):
        sq(float('inf'))

def test_squareroot():
    sqrt = SquareRoot()
    assert sqrt(4) == 2
    assert sqrt(1) == 1
    with pytest.raises(ValueError):
        sqrt(-1)
    with pytest.raises(ValueError):
        sqrt(float('inf'))

@pytest.mark.parametrize("operation, a, b, expected", [
    (Addition(), 2, 3, 5),
    (Subtraction(), 5, 3, 2),
    (Multiplication(), 2, 3, 6),
    (Division(), 6, 3, 2)
])
def test_basic_operations(operation, a, b, expected):
    assert operation(a, b) == expected

@pytest.mark.parametrize("operation", [Addition(), Subtraction(), Multiplication(), Division()])
def test_edge_cases(operation):
    with pytest.raises(ValueError):
        if isinstance(operation, (Addition, Subtraction, Multiplication)):
            operation(float('inf'), float('inf'))
        elif isinstance(operation, Division):
            operation(1, 0)