# Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.


# use exponentiation by squaring algorithm

def pow(b, e):

    # base case: b ^ 0 = 1
    if e == 0:
        return 1
    
    # if e is even, use the identity: b ^ e = (b ^ (e/2)) ^ 2
    if e % 2 == 0:
        # RECURSION to reduce the problem by divifing the exponent by 2 in each recursive call
        # divide the exponent by 2 and round down to the nearest integer
        result = pow(b, e // 2)

        # square the result 
        return result * result
    
    # if e is odd, use the identity: b ^ e = b * (b ^ (e - 1))
    else:
        result = pow(b, (e - 1) // 2)
        return b * result * result 

def ask():

    a = int(input("First number: "))
    b = int(input("Second number: "))

    result = pow(a, b)
    print(result)

if __name__ == '__main__':
    
    ask()

