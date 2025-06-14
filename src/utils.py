from typing import Union

def validate_numeric_input(value: Union[int, float, str]) -> float:
    """
    Validate and convert input to float.
    
    Args:
        value: The input value to validate
        
    Returns:
        float: The converted numeric value
        
    Raises:
        ValueError: If the input cannot be converted to a number
    """
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(value.strip())
    except (ValueError, AttributeError):
        raise ValueError(f"Invalid numeric input: {value}")

def format_result(value: float, decimal_places: int = 2) -> str:
    """
    Format the numeric result with specified decimal places.
    
    Args:
        value: The numeric value to format
        decimal_places: Number of decimal places to round to
        
    Returns:
        str: Formatted string representation of the number
    """
    return f"{value:.{decimal_places}f}"
