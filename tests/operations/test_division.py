import pytest
from src.operations.division import Division

def test_division():
    assert Division.execute(6, 2) == 3
    assert Division.execute(5, 2) == 2.5
    assert Division.execute(0, 5) == 0

def test_division_by_zero():
    with pytest.raises(ValueError):
        Division.execute(5, 0)
