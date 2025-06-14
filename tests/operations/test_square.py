import pytest
from src.operations.square import Square

def test_square():
    assert Square.execute(2) == 4
    assert Square.execute(-2) == 4
    assert Square.execute(0) == 0
    assert Square.execute(2.5) == 6.25
