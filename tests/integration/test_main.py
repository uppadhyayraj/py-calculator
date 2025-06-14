import pytest
from unittest.mock import patch
from src.main import main
from src.calculator import Calculator

def test_main_addition(capsys):
    # Test addition operation
    with patch('builtins.input', side_effect=['1', '5', '3', '5']):
        main()
    captured = capsys.readouterr()
    assert "Addition Result: 8.00" in captured.out

def test_main_division(capsys):
    # Test division operation
    with patch('builtins.input', side_effect=['4', '10', '2', '5']):
        main()
    captured = capsys.readouterr()
    assert "Division Result: 5.00" in captured.out

def test_main_invalid_input(capsys):
    # Test invalid numeric input
    with patch('builtins.input', side_effect=['1', 'abc', '1', '2', '3', '5']):
        main()
    captured = capsys.readouterr()
    assert "Error: Invalid numeric input" in captured.out

def test_main_division_by_zero(capsys):
    # Test division by zero
    with patch('builtins.input', side_effect=['4', '10', '0', '5']):
        main()
    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out
