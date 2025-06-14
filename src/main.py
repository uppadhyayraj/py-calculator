from src.calculator import Calculator
from src.utils import validate_numeric_input, format_result

def main():
    """Main function to run the calculator program."""
    calculator = Calculator()
    
    operations = {
        '1': ('Addition', calculator.add),
        '2': ('Subtraction', calculator.subtract),
        '3': ('Multiplication', calculator.multiply),
        '4': ('Division', calculator.divide)
    }
    
    while True:
        print("\nSimple Calculator")
        print("----------------")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")
        
        choice = input("\nSelect operation (1-5): ").strip()
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice not in operations:
            print("Invalid choice! Please try again.")
            continue
            
        try:
            x = validate_numeric_input(input("Enter first number: "))
            y = validate_numeric_input(input("Enter second number: "))
            
            operation_name, operation_func = operations[choice]
            result = operation_func(x, y)
            
            print(f"\n{operation_name} Result: {format_result(result)}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
