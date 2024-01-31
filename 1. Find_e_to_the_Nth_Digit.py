import math

# e = 2.718281828459045


import math

def get_number():

    while True:
        # keep asking for a number 
        try:
            n = int(input("Enter a number lower than 50: "))
            if n < 51:
                print(f"Euler number to {n} digits is {math.e:.{n}f}")
                break  # exit the loop if a valid number is provided

            else:
                print("Please enter a number lower than 50.")

        except ValueError:
            print("Provide an integer.")

get_number()




