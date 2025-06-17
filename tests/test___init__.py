python
import pytest

from src.operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

# Test Addition class
def test_addition_positive_numbers():
    assert Addition(2, 3).calculate() == 5

def test_addition_negative_numbers():
    assert Addition(-1, -1).calculate() == -2

# Test Subtraction class
def test_subtraction_positive_numbers():
    assert Subtraction(5, 3).calculate() == 2

def test_subtraction_negative_numbers():
    assert Subtraction(-2, -4).calculate() == 2

# Test Multiplication class
def test_multiplication_positive_numbers():
    assert Multiplication(4, 3).calculate() == 12

def test_multiplication_large_numbers():
    assert Multiplication(10**6, 10**6).calculate() == 10**12

# Test Division class
def test_division_positive_numbers():
    assert Division(10, 2).calculate() == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division(10, 0).calculate()

# Test Square class
def test_square_positive_number():
    assert Square(4).calculate() == 16

def test_square_negative_number():
    assert Square(-3).calculate() == 9

# Test SquareRoot class
def test_square_root_positive_number():
    assert SquareRoot(16).calculate() == 4

def test_square_root_negative_number():
    with pytest.raises(ValueError):
        SquareRoot(-4).calculate()