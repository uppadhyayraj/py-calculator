import pytest
from src.utils import validate_numeric_input, format_result

def test_validate_numeric_input_valid():
    assert validate_numeric_input(5) == 5.0
    assert validate_numeric_input(3.14) == 3.14
    assert validate_numeric_input("42") == 42.0
    assert validate_numeric_input("3.14") == 3.14
    assert validate_numeric_input(" 42 ") == 42.0

def test_validate_numeric_input_invalid():
    invalid_inputs = ["abc", "", None, "12.34.56", "1+2"]
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError):
            validate_numeric_input(invalid_input)

def test_format_result():
    assert format_result(3.14159) == "3.14"
    assert format_result(3.14159, decimal_places=3) == "3.142"
    assert format_result(42) == "42.00"
    assert format_result(42.0) == "42.00"
    assert format_result(42.1, decimal_places=0) == "42"
