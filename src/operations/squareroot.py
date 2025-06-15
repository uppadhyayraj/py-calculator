from math import sqrt

class SquareRoot:
    @staticmethod
    def execute(x: float) -> float:
        """Calculate the square root of a number.
        
        Args:
            x: The number to find square root of
            
        Returns:
            float: The square root of the input number
            
        Raises:
            ValueError: If input is negative
        """
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return sqrt(x)
