import os

# code begins
clear = lambda: os.system('cls')
clear()

def even(num):
    if num % 10 == 0:
        return True
    else: return False
    
res = even(int(input("Input number: ")))
print(res)