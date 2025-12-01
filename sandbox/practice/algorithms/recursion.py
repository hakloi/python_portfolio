import os

# code begins
clear = lambda: os.system('cls')
clear() 

def factorial(n):
    if n < 1:   #base case
        return 1
    else:
        returnNumber = n * factorial(n - 1)  # recursive case
        print(str(n) + '! = ' + str(returnNumber))
        return returnNumber
    
print(factorial(8))

# ---------------

def fac(n):
    return 1 if (n < 1) else n * fac(n-1)

print(fac(8))