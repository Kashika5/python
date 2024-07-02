def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Welcome to Simple Calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Operations available:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            operation = input("Choose an operation (1/2/3/4): ")

            if operation == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid operation! Please choose 1, 2, 3, or 4.")

            again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    print("Thank you for using Simple Calculator!")

# Start the calculator
calculator()
