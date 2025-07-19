def calculator():
    print("Simple Calculator")

    try:
        # Input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Input operation
        print("Choose an operation:")
        print(" +  → Addition")
        print(" -  → Subtraction")
        print(" *  → Multiplication")
        print(" /  → Division")
        operation = input("Enter operation (+, -, *, /): ")

        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print(" Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print(" Error: Invalid operation selected.")
            return

        print(f" Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print(" Error: Please enter valid numbers.")

while True:
    calculator()
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the calculator!")
        break
