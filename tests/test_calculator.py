python
import pytest
from unittest.mock import patch

# Mocking the operations classes
class MockAddition:
    @staticmethod
    def execute(x, y):
        return x + y

class MockSubtraction:
    @staticmethod
    def execute(x, y):
        return x - y

class MockMultiplication:
    @staticmethod
    def execute(x, y):
        return x * y

class MockDivision:
    @staticmethod
    def execute(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

class MockSquare:
    @staticmethod
    def execute(x):
        return x ** 2

class MockSquareRoot:
    @staticmethod
    def execute(x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number")
        return x ** 0.5

# Patching the operations classes in the Calculator class
@patch('src.calculator.Addition', new=MockAddition)
@patch('src.calculator.Subtraction', new=MockSubtraction)
@patch('src.calculator.Multiplication', new=MockMultiplication)
@patch('src.calculator.Division', new=MockDivision)
@patch('src.calculator.Square', new=MockSquare)
@patch('src.calculator.SquareRoot', new=MockSquareRoot)

def test_calculator_add():
    calculator = Calculator()
    assert calculator.add(2, 3) == 5

def test_calculator_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 2) == 3

def test_calculator_multiply():
    calculator = Calculator()
    assert calculator.multiply(4, 3) == 12

def test_calculator_divide():
    calculator = Calculator()
    assert calculator.divide(8, 2) == 4
    with pytest.raises(ValueError):
        calculator.divide(1, 0)

def test_calculator_square():
    calculator = Calculator()
    assert calculator.square(5) == 25

def test_calculator_sqrt():
    calculator = Calculator()
    assert calculator.sqrt(9) == 3
    with pytest.raises(ValueError):
        calculator.sqrt(-4)