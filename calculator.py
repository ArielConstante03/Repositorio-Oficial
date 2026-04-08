# Simple Calculator Program

def calculator():
    """A simple calculator that performs basic arithmetic operations."""
    
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    print("\nSupported operations: +, -, *, /")
    print("Example: 10 + 5 or 20 * 3")
    print("\nType 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("Enter calculation (e.g., 5 + 3): ").strip()
            
            # Check if user wants to quit
            if user_input.lower() == 'quit':
                print("\nThank you for using Calculator! Goodbye!")
                break
            
            # Evaluate the expression
            result = eval(user_input)
            print(f"Result: {result}\n")
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!\n")
        except Exception as e:
            print(f"Error: Invalid input. Please enter a valid expression.\n")


if __name__ == "__main__":
    calculator()
