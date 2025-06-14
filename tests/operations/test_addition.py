import pytest
from src.operations.addition import Addition

def test_addition():
    assert Addition.execute(2, 3) == 5
    assert Addition.execute(-1, 1) == 0
    assert Addition.execute(0, 0) == 0
    assert Addition.execute(2.5, 3.5) == 6.0
