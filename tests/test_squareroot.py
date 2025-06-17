python
import pytest
from unittest.mock import patch
from src.operations.squareroot import SquareRoot

def test_execute_positive_input():
    assert SquareRoot.execute(4.0) == 2.0
    assert SquareRoot.execute(16.0) == 4.0
    assert SquareRoot.execute(1.0) == 1.0

@patch('math.sqrt')
def test_execute_zero_input(mock_sqrt):
    mock_sqrt.return_value = 0.0
    assert SquareRoot.execute(0.0) == 0.0

def test_execute_negative_input():
    with pytest.raises(ValueError):
        SquareRoot.execute(-1.0)

@patch('math.sqrt')
def test_execute_small_positive_number(mock_sqrt):
    mock_sqrt.return_value = 0.1
    assert SquareRoot.execute(0.01) == 0.1

@patch('math.sqrt')
def test_execute_large_positive_number(mock_sqrt):
    mock_sqrt.return_value = 1000.0
    assert SquareRoot.execute(1000000.0) == 1000.0