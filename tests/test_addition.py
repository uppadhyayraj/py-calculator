import pytest
from src.operations.addition import Addition

class TestAddition:
    def test_execute(self):
        addition = Addition()
        assert addition.execute(10, 5) == 15
        assert addition.execute(-10, -5) == -15
        assert addition.execute(10, -5) == 15
        assert addition.execute(-10, 5) == -15