import pytest
from src.operations import squareroot

def test_execute():
    # Test with positive number
    assert round(squareroot.SquareRoot().execute(9), 5) == 3.0
    
    # Test with zero
    assert round(squareroot.SquareRoot().execute(0), 5) == 0.0
    
    # Test with negative number
    with pytest.raises(ValueError):
        squareroot.SquareRoot().execute(-1)
        
    # Test with null/empty inputs
    with pytest.raises(TypeError):
        squareroot.SquareRoot().execute()