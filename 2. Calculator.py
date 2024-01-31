# A simple calculator to do basic operators. Make it a scientific calculator for added complexity.


# operations

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def calculator():

    # starting value
    result = 0

    while True:

        try:

            number = int(input("Number: "))
            print(f"Result: {result}")
            operator = input("Operator +, -, /, *, c, x: ")
            if operator == '+':
                result +=  number

            elif operator == '-':
                result -= number

            elif operator == '*':
                result *= number

            elif operator == '/':
                if number != 0:  # check for division by zero
                    result /= number
                else:
                    print("Cannot divide by zero.")

            elif operator == 'c':
                # reset the starting value
                result = 0

            elif operator == 'x':
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
calculator()
