python
import pytest
from src.operations.addition import Addition

class TestAddition:
    def setup(self):
        self.addition = Addition()
    
    def teardown(self):
        del self.addition
    
    @pytest.mark.parametrize("x, y, result", [
        (1.0, 2.0, 3.0),
        (-1.0, -2.0, -3.0)
    ])
    def test_execute_with_valid_numbers(self, x, y, result):
        assert self.addition.execute(x, y) == result
        
    @pytest.mark.parametrize("x, y", [
        (1.0, None),
        (None, 2.0),
        ("a", "b")
    ])
    def test_execute_with_invalid_inputs(self, x, y):
        with pytest.raises(TypeError):
            self.addition.execute(x, y)
        
    @pytest.mark.parametrize("x, y", [
        (1.0, 2.0),
        (-1.0, -2.0)
    ])
    def test_performance(self, x, y):
        assert self.addition.execute(x, y) == x + y