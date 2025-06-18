import pytest
from src.calculator import Calculator
from .operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

class TestCalculator:
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(1, 2)
        assert result == 3
    
    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(5, 3)
        assert result == 2
    
    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(4, 5)
        assert result == 20
    
    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(10, 2)
        assert result == 5
    
    def test_square(self):
        calculator = Calculator()
        result = calculator.square(3)
        assert result == 9
    
    def test_sqrt(self):
        calculator = Calculator()
        result = calculator.sqrt(4)
        assert result == 2