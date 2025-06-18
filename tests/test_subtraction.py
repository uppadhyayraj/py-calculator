import pytest
from src.operations.subtraction import Subtraction

class TestSubtraction:
    def test_execute(self):
        # Positive case 1: Subtracting two positive numbers
        x = 10.0
        y = 5.0
        expected_output = 5.0
        assert Subtraction.execute(x, y) == expected_output

        # Positive case 2: Subtracting a negative number from a positive number
        x = 10.0
        y = -5.0
        expected_output = 15.0
        assert Subtraction.execute(x, y) == expected_output

        # Positive case 3: Subtracting two negative numbers
        x = -10.0
        y = -5.0
        expected_output = -15.0
        assert Subtraction.execute(x, y) == expected_output

        # Negative case 1: Testing the execute method with invalid inputs
        x = "hello"
        y = "world"
        expected_output = None
        assert Subtraction.execute(x, y) == expected_output