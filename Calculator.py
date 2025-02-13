# Rayan Alam
# 100908385
# Activity 6B1

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice! Please select a valid option.")

        next_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calc != 'yes':
            print("Goodbye!")
            break

# Running the calculator function
calculator()