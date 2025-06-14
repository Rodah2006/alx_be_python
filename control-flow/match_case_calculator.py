# Step 1: Prompt user for first number
num1 = float(input("Enter the first number: "))

# Step 2: Prompt user for second number
num2 = float(input("Enter the second number: "))

# Step 3: Ask user to choose operation
operation = input("Choose the operation (+, -, *, /): ")

# Step 4: Use match case to perform operation and handle division by zero
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation selected.")
