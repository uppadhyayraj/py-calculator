import pytest
from src.calculator import Calculator
from unittest.mock import Mock

# Mocking external dependencies
Addition = Mock()
Subtraction = Mock()
Multiplication = Mock()
Division = Mock()
Square = Mock()
SquareRoot = Mock()

def test_add():
    calculator = Calculator()
    Addition.execute.return_value = 10
    
    assert calculator.add(5, 5) == 10
    Addition.execute.assert_called_once_with(5, 5)

def test_subtract():
    calculator = Calculator()
    Subtraction.execute.return_value = 2
    
    assert calculator.subtract(10, 8) == 2
    Subtraction.execute.assert_called_once_with(10, 8)

def test_multiply():
    calculator = Calculator()
    Multiplication.execute.return_value = 40
    
    assert calculator.multiply(5, 8) == 40
    Multiplication.execute.assert_called_once_with(5, 8)

def test_divide():
    calculator = Calculator()
    Division.execute.return_value = 2.5
    
    assert calculator.divide(10, 4) == 2.5
    Division.execute.assert_called_once_with(10, 4)

def test_square():
    calculator = Calculator()
    Square.execute.return_value = 16
    
    assert calculator.square(4) == 16
    Square.execute.assert_called_once_with(4)

def test_sqrt():
    calculator = Calculator()
    SquareRoot.execute.return_value = 2
    
    assert calculator.sqrt(4) == 2
    SquareRoot.execute.assert_called_once_with(4)

# Testing with null/empty inputs and boundary conditions
def test_add_null():
    calculator = Calculator()
    with pytest.raises(TypeError):
        calculator.add("a", 5)
        
def test_subtract_null():
    calculator = Calculator()
    with pytest.raises(TypeError):
        calculator.subtract("a", 5)
        
# and so on for other functions...