import pytest
from src.calculator import Calculator
from .operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

class TestCalculator:
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        yield  # this is where the test runs
        
    def test_add_positive_numbers(self):
        calc = Calculator()
        assert calc.add(2, 3) == Addition.execute(2, 3)
    
    def test_subtract_negative_numbers(self):
        calc = Calculator()
        assert calc.subtract(-5, -3) == Subtraction.execute(-5, -3)
    
    def test_multiply_with_zero(self):
        calc = Calculator()
        assert calc.multiply(0, 7) == Multiplication.execute(0, 7)
    
    def test_divide_by_non_zero(self):
        calc = Calculator()
        assert calc.divide(10, 2) == Division.execute(10, 2)
    
    def test_square_positive_number(self):
        calc = Calculator()
        assert calc.square(3) == Square.execute(3)
    
    def test_sqrt_perfect_square(self):
        calc = Calculator()
        assert calc.sqrt(9) == SquareRoot.execute(9)
    
    @pytest.mark.parametrize("x, y", [
        (10**10, 10**10),  # Adding two large numbers to check for potential overflow issues
        (-5, -3),          # Subtracting negative numbers
        (0, 7),            # Multiplying by zero
        (10, 2),           # Dividing non-zero by a number
        (3, 3)             # Squaring and square rooting perfect squares
    ])
    def test_calculator_operations(self, x, y):
        calc = Calculator()
        if isinstance(x, int) and isinstance(y, int):
            assert calc.add(x, y) == Addition.execute(x, y)
            assert calc.subtract(x, y) == Subtraction.execute(x, y)
            assert calc.multiply(x, y) == Multiplication.execute(x, y)
            if y != 0:
                assert calc.divide(x, y) == Division.execute(x, y)
            if x >= 0:
                assert calc.square(x) == Square.execute(x)
                assert calc.sqrt(x) == SquareRoot.execute(x)
    
    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ZeroDivisionError):
            calc.divide(10, 0)
    
    def test_sqrt_negative_number(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.sqrt(-1)