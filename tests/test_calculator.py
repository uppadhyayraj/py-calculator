python
import pytest
from unittest.mock import patch

from src.calculator import Calculator
from src.operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

@pytest.fixture
def calculator():
    return Calculator()

@patch('src.operations.Addition.execute')
def test_add(mock_addition, calculator):
    mock_addition.return_value = 5
    result = calculator.add(2, 3)
    assert result == 5
    mock_addition.assert_called_once_with(2, 3)

@patch('src.operations.Subtraction.execute')
def test_subtract(mock_subtraction, calculator):
    mock_subtraction.return_value = 6
    result = calculator.subtract(10, 4)
    assert result == 6
    mock_subtraction.assert_called_once_with(10, 4)

@patch('src.operations.Multiplication.execute')
def test_multiply(mock_multiplication, calculator):
    mock_multiplication.return_value = 21
    result = calculator.multiply(3, 7)
    assert result == 21
    mock_multiplication.assert_called_once_with(3, 7)

@patch('src.operations.Division.execute')
def test_divide(mock_division, calculator):
    mock_division.return_value = 2
    result = calculator.divide(8, 4)
    assert result == 2
    mock_division.assert_called_once_with(8, 4)

@patch('src.operations.Division.execute')
def test_divide_by_zero(mock_division, calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)

@patch('src.operations.Square.execute')
def test_square(mock_square, calculator):
    mock_square.return_value = 25
    result = calculator.square(5)
    assert result == 25
    mock_square.assert_called_once_with(5)

@patch('src.operations.SquareRoot.execute')
def test_sqrt(mock_sqrt, calculator):
    mock_sqrt.return_value = 3
    result = calculator.sqrt(9)
    assert result == 3
    mock_sqrt.assert_called_once_with(9)

@patch('src.operations.SquareRoot.execute')
def test_sqrt_negative_number(mock_sqrt, calculator):
    with pytest.raises(ValueError):
        calculator.sqrt(-4)