# Напишите программу, которая создает два списка чисел,
# (случайной длины от 50 до 100), (заполняя списки случайными
# числами от 0 до 9999). И выводит все элементы первого,
# которых нет во втором.
import os
import random

# code begins
clear = lambda: os.system('cls')
clear()

l1 = [random.randrange(0, 99) for _ in range(50, 100)]
l2 = [random.randrange(0, 99) for _ in range(50, 100)]
print("The 1st list:\n",  l1)
print("\nThe 2nd list:\n", l2, "\n")

# отличие set от frozenset
# set - изменяемый тип данных, а frozenset - нет
def matches_lists(l1,l2):
    matches = set(l1).intersection(l2)
    if matches is None:
        print("There is no matches between lists.")
    else:
        print("Matches: ", matches)

matches_lists(l1,l2)
