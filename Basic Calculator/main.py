number1 = float(input("Enter first operand: "))
number2 = float(input("Enter second operand: "))
operator = input("Enter your Operator ( +, -, *, /): ")

while True:
    if ( operator == "+"):
        print( number1 + number2)
        break

    elif ( operator == "-"):
        print( number1 - number2)
        break

    elif ( operator == "*"):
        print( number1 * number2)
        break

    elif ( operator == "/"):
        if ( number2 == 0):
            print("Error: Division by zero is not allowed")
            break
        print( number1 / number2)
        break

    else:
        print("Something went wrong!")
        
