python
import pytest
from src.operations.subtraction import Subtraction

class TestSubtraction:
    def test_execute_with_integers(self):
        assert Subtraction.execute(5, 3) == 2
        assert Subtraction.execute(1, 1) == 0
        assert Subtraction.execute(0, 5) == -5
        
    def test_execute_with_floats(self):
        assert Subtraction.execute(2.5, 1.0) == 1.5
        
    def test_execute_with_zero(self):
        assert Subtraction.execute(5, 0) == 5
        assert Subtraction.execute(0, 0) == 0
        
    def test_execute_with_negative_numbers(self):
        assert Subtraction.execute(-1, -1) == 0
        assert Subtraction.execute(2, -3) == 5
        
    def test_error_handling_for_non_numeric_inputs(self):
        with pytest.raises(ValueError):
            Subtraction.execute("5", "3")
        
    @pytest.fixture(scope='module')
    def setup_teardown():
        # Setup and teardown for tests
        pass
    
    def test_performance_with_integers(self):
        assert Subtraction.execute(5, 3) == 2
        
    def test_performance_with_floats(self):
        assert Subtraction.execute(2.5, 1.0) == 1.5