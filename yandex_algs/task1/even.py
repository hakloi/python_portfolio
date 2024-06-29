import os

# code begins
clear = lambda: os.system('cls')
clear()


# binary
def binary_even(num):
    if num % 10 == 0:
        return True
    else: return False
    
res = binary_even(int(input("Input number: ")))
print(res)