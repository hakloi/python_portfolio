# Дана последовательность случайных чисел, от 0 до 9999, 
# случайной длины (от 5 до 100) и положительное число Х, больше нуля. 
# Напишите функцию magic(), принимающую эти аргументы, и выясните,
# можно ли разделить сумму чисел последовательности на число  Х без остатка. 
# В качестве ответа возвращается bool, если можно то True иначе False.

import os
import random

# code begins
clear = lambda: os.system('cls')
clear()
        
def magic(num,l1):
    a = sum(l1)
    b = a/num
    print("Problem:", a, ":", num, "=", b)
    if (a%num == 0):
        print("There is no remainder of the division.\n\n" + str(True))
    else:
        print("There is remainder of the division.\n\n" + str(False))
        
l1 = [random.randrange(5,100) for _ in range(0,99)]
num = int(input("Positive number: "))
magic(num, l1)