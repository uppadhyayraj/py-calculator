python
import pytest
from src.operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

# Test Addition class
def test_addition_positive_integers():
    assert Addition(2, 3).calculate() == 5

def test_addition_negative_integers():
    assert Addition(-1, -1).calculate() == -2

def test_addition_mixed_integers():
    assert Addition(2, -1).calculate() == 1

# Test Subtraction class
def test_subtraction_positive_integers():
    assert Subtraction(5, 3).calculate() == 2

def test_subtraction_negative_integers():
    assert Subtraction(-1, -3).calculate() == 2

def test_subtraction_mixed_integers():
    assert Subtraction(2, -1).calculate() == 3

# Test Multiplication class
def test_multiplication_positive_integers():
    assert Multiplication(2, 3).calculate() == 6

def test_multiplication_negative_integers():
    assert Multiplication(-1, -3).calculate() == 3

def test_multiplication_mixed_integers():
    assert Multiplication(2, -1).calculate() == -2

# Test Division class
def test_division_positive_integers():
    assert Division(6, 3).calculate() == 2

def test_division_negative_integers():
    assert Division(-6, -3).calculate() == 2

def test_division_mixed_integers():
    assert Division(6, -3).calculate() == -2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division(1, 0).calculate()

# Test Square class
def test_square_positive_integer():
    assert Square(2).calculate() == 4

def test_square_negative_integer():
    assert Square(-2).calculate() == 4

def test_square_mixed_integers():
    assert Square(2.5).calculate() == 6.25

# Test SquareRoot class
def test_sqrt_positive_integer():
    assert SquareRoot(4).calculate() == 2

def test_sqrt_negative_integer():
    with pytest.raises(ValueError):
        SquareRoot(-1).calculate()

def test_sqrt_mixed_integers():
    assert SquareRoot(2.25).calculate() == 1.5