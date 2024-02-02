# Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.

def ask():

    a = int(input("First number: "))
    b = int(input("Second number: "))

    print(pow(a, b))

ask()