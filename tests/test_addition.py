import pytest
from src.operations.addition import Addition

def test_addition_positive():
    result = Addition.execute(3.0, 2.0)
    assert result == 5.0

def test_addition_positive_negative():
    result = Addition.execute(3.0, -2.0)
    assert result == 1.0

def test_addition_negative():
    result = Addition.execute(-3.0, -2.0)
    assert result == -5.0

def test_addition_zero():
    result = Addition.execute(3.0, 0.0)
    assert result == 3.0