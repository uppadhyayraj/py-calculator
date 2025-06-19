import pytest
from src.operations import addition

# Edge Cases
def test_addition_edge_cases():
    assert addition.Addition.execute(5.2, -3.4) == 1.8

# Test Scenarios
def test_positive_numbers():
    assert addition.Addition.execute(5.2, 3.4) == 8.6

def test_negative_numbers():
    assert addition.Addition.execute(-5.2, -3.4) == -1.8

def test_zero():
    assert addition.Addition.execute(0, 5.6) == 5.6