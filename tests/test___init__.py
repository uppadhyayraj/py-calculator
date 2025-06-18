import pytest
from src.operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

class TestOperations:
    def test_addition(self):
        assert Addition().calculate(1, 1) == 2
        assert Addition().calculate(2, 2) == 4
        assert Addition().calculate(3, 3) == 6
    
    def test_subtraction(self):
        assert Subtraction().calculate(1, 1) == 0
        assert Subtraction().calculate(2, 2) == 0
        assert Subtraction().calculate(3, 3) == 0
    
    def test_multiplication(self):
        assert Multiplication().calculate(1, 1) == 1
        assert Multiplication().calculate(2, 2) == 4
        assert Multiplication().calculate(3, 3) == 9
    
    def test_division(self):
        assert Division().calculate(1, 1) == 1
        assert Division().calculate(2, 2) == 1
        assert Division().calculate(3, 3) == 1
    
    def test_square(self):
        assert Square().calculate(0) == 0
        assert Square().calculate(1) == 1
        assert Square().calculate(2) == 4
    
    def test_squareroot(self):
        assert SquareRoot().calculate(0) == 0
        assert SquareRoot().calculate(1) == 1
        assert SquareRoot().calculate(2) == 1.4142135623730951