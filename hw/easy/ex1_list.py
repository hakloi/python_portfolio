# Напишите программу, которая создает два списка чисел,
# (случайной длины от 50 до 100), (заполняя списки случайными
# числами от 0 до 9999). И выводит все элементы первого,
# которых нет во втором.

# с теми же списками чисел, нужно вернуть список,
# который состоит из элементов, общих для этих двух списков.
# В цикле идем по 1 списку и проверяем есть ли текущий элемент
# во втором, если есть добавляем в результат, результат печатаем.

import os
import random

# code begins
clear = lambda: os.system('cls')
clear()

l1 = [random.randrange(0, 9999) for _ in range(50, 100)]
l2 = [random.randrange(0, 9999) for _ in range(50, 100)]
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


# лучше проверять на randrange(0,90),
# иначе вероятность совпадений минимальная
matches_lists(l1,l2)

def non_match_elements(l1, l2):
    non_match = []
    for i in l1:
        if i not in l2:
            non_match.append(i)
    return print("\nNo match elements: ", non_match)


non_match_elements(l1,l2)