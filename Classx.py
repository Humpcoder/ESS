def calculator():
    print("Simple Calculator")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            # Get user input
            operation = input("Enter operation (1-5 or +,-,*,/): ")
            
            if operation in ['5', 'exit', 'Exit']:
                print("Goodbye!")
                break
            
            if operation in ['1', '+']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operation in ['2', '-']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operation in ['3', '*']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operation in ['4', '/']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Invalid operation. Please try again.")
            
            print()  # Add empty line for better readability
            
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")

if __name__ == "__main__":
    calculator()