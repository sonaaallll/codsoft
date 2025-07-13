
def calculator():
    print("Welcome to the simple calculator!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter operation (1/2/3/4): ")
    

    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation selected.")
calculator()


