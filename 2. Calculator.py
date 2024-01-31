# A simple calculator to do basic operators. Make it a scientific calculator for added complexity.


def calculator():

    # starting value
    result = 0

    while True:

        try:

            previous_number = result 

            operator = input("Operator +, -, /, *, c, x: ")

            # break the loop when 'x' is entered
            if operator == 'x':
                break

            if operator == 'c':
                result = 0
            else:

                number = int(input("Number: "))

                if operator == '+':
                    result += number

                elif operator == '-':
                    result -= number

                elif operator == '*':
                    result *= number

                elif operator == '/':
                    if number != 0:  # check for division by zero
                        result /= number
                    else:
                        print("Cannot divide by zero.")

                print(f"{previous_number} {operator} {number} = {result}")
                print('\n')

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    
calculator()
