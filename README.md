# Simple Python Calculator - README

## Overview
This is a simple command-line calculator written in Python. It performs basic arithmetic operations including addition, subtraction, multiplication, and division.

## Features
- **Basic Operations**: Supports +, -, *, /
- **User-friendly Interface**: Clear menu and prompts
- **Error Handling**: 
  - Prevents division by zero
  - Validates numeric inputs
- **Flexible Input**: Accepts both numbers (1-4) and symbols (+, -, *, /) for operations
- **Exit Option**: Clean program termination

## Requirements
- Python 3.x

## Installation
No installation required. Simply download or copy the Python script.

## Usage
1. Run the script in your terminal/command prompt:
   ```bash
   python calculator.py
   ```
2. Follow the on-screen instructions:
   - Choose an operation (1-5 or +,-,*,/)
   - Enter numbers when prompted
   - View the result
3. Select option 5 or type 'exit' to quit

## Code Structure
- Main function `calculator()` handles all operations
- Continuous loop until user chooses to exit
- Try-except blocks for error handling
- Clear formatting with empty lines between operations

## Example Usage
```
Simple Calculator
Operations available:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Enter operation (1-5 or +,-,*,/): +
Enter first number: 5
Enter second number: 3
Result: 5.0 + 3.0 = 8.0
```

## Limitations
- Currently only handles two operands per operation
- No support for more complex operations (exponents, roots, etc.)
- No memory function

## Possible Enhancements
- Add support for more operations
- Implement calculation history
- Add GUI interface
- Support for multiple consecutive operations

## License
This project is open-source and free to use.
