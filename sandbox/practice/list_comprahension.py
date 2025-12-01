# list compehension, min, max, sum

# Суммирование миллиона чисел: создайте список чисел от 1 до 1 000 000,
# затем воспользуйтесь функциями min() и max() и убедитесь в том,
# что список действительно начинается с 1 и заканчивается 1 000 000 .
# Вызовите функцию sum() и посмотрите, насколько 
# быстро Python сможет просуммировать миллион чисел 
import os

# code begins
clear = lambda: os.system('cls')
clear()

def max_min_sum_of_list(l1):
    print("\nMin num:", min(l1))
    print("\nMax num:", max(l1))
    print("\nSum:", sum(l1))
    
start = int(input("Write the first number of list: "))
the_end = int(input("Write the last number of list: "))
step = int(input("Write step of your list: "))

l1 = list(range(start,the_end, step))
max_min_sum_of_list(l1)