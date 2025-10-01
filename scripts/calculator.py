# calculator.py

# Ask for the first number
num1 = float(input("Enter the first number: "))

# Ask for the second number
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
        # Prevent division by zero
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation"

if result > 25:
    output = "HUGE"
else:
    output = result

print("Result:", output)