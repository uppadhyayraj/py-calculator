from .operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

class Calculator:
    """A simple calculator class that uses separate operation classes."""
    
    def add(self, x: float, y: float) -> float:
        """Add two numbers."""
        return Addition.execute(x, y)
    
    def subtract(self, x: float, y: float) -> float:
        """Subtract two numbers."""
        return Subtraction.execute(x, y)
    
    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        return Multiplication.execute(x, y)
    
    def divide(self, x: float, y: float) -> float:
        """Divide two numbers."""
        return Division.execute(x, y)
    
    def square(self, x: float) -> float:
        """Calculate the square of a number."""
        return Square.execute(x)
        
    def sqrt(self, x: float) -> float:
        """Calculate the square root of a number."""
        return SquareRoot.execute(x)
