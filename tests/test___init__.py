python
import pytest

from src.operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

# Test Addition class
def test_addition_positive_integers():
    assert Addition(2, 3).calculate() == 5

def test_addition_negative_integers():
    assert Addition(-1, -2).calculate() == -3

# Test Subtraction class
def test_subtraction_positive_integers():
    assert Subtraction(5, 3).calculate() == 2

def test_subtraction_negative_integers():
    assert Subtraction(-2, -4).calculate() == 2

# Test Multiplication class
def test_multiplication_floating_point_numbers():
    assert Multiplication(0.5, 2.5).calculate() == 1.25

def test_multiplication_large_numbers():
    assert Multiplication(1e9, 1e9).calculate() == 1e18

# Test Division class
def test_division_positive_integers():
    assert Division(10, 2).calculate() == 5

def test_division_negative_integers():
    assert Division(-6, -3).calculate() == 2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division(5, 0).calculate()

# Test Square class
def test_square_of_zero_and_one():
    assert Square(0).calculate() == 0
    assert Square(1).calculate() == 1

def test_square_large_numbers():
    assert Square(1e6).calculate() == 1e12

# Test SquareRoot class
def test_square_root_perfect_squares():
    assert SquareRoot(4).calculate() == 2
    assert SquareRoot(9).calculate() == 3

def test_square_root_negative_numbers():
    with pytest.raises(ValueError):
        SquareRoot(-4).calculate()