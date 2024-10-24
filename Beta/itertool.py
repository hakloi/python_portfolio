import os

os.system('cls')

# print(itertools.product("ABC", repeat=2))

# from itertools import count

# for value in count(0, 0.1):
#     if value <= 1:
#         print(round(value, 1))
#     else:
#         break

# s = list(input().split())

# for index, value in enumerate(s, 1):
#     print(f"{index}. {value}")

# Аня, Вова
# Боря, Дима, Гена

# first = input().split(", ")
# second = input().split(", ")

# for child1, child2 in zip(first, second):
#     print(f"{child1} - {child2}")

# import itertools

# nums = list(map(float, input().split()))
# c2 = itertools.count(nums[0], nums[2])
# for i in c2:
#     if i > nums[1]:
#         break
#     print(str(round(i, 2)), sep='\n')
    
# 3.2 6.4 0.8
# 3.20
# 4.00
# 4.80
# 5.60
# 6.40

# import itertools

# def concat_words(x, y):
#     return x + " " + y


# words = input().split()
# for line in itertools.accumulate(words, concat_words):
#     print(line)
    
    
# картина, корзина, картонка
# мыло, манка
# молоко, хлеб, сыр

# import itertools

# m = input().split(", ")
# p = input().split(", ")
# d = input().split(", ")

# res = itertools.chain(m, p, d)
# for i, v in enumerate(sorted(list(res)), 1):
#     print(f"{i}. {v}")

# from itertools import product
# suit = input()

# nominals = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
# suits = ["пик", "бубен", "червей", "треф"]

# suits.remove(suit)

# for s, n in product(nominals, suits):
#     print(f"{s} {n}")

# from itertools import *

# n = int(input())
# names = []

# for i in range(n):
#     name = input()
#     names.append(name)

# for i in combinations(names, 2):
#     print(*i, sep=" - ") 


# Аня - Боря
# Аня - Вова
# Боря - Вова

# from itertools import islice, cycle
# m = int(input())

# porridge = list(input() for _ in range(m))

# n = int(input())
# res = list(islice(porridge, 0, n))

# count = 0
# for i in cycle(porridge):
#     if count < n:
#         print(i)
#         count += 1
#     else:
#         break


# l2=itertools.cycle(l1)
# print (l2)#Output:<itertools.cycle object at 0x02F794E8>

# count=0
# for i in l2:
#     #It will end in infinite loop. So have to define terminating condition.
#     if count > 15:
#         break
#     else:
#         print (i,end=" ")#Output:1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1
#         count+=1


# ввод
# 5
# Манная
# Гречневая
# Пшённая
# Овсяная
# Рисовая
# 12

# вывод
# Манная
# Гречневая
# Пшённая
# Овсяная
# Рисовая
# Манная
# Гречневая
# Пшённая
# Овсяная
# Рисовая
# Манная
# Гречневая


#  x = ['a', 'b', 'c']
# >>> y = ['1', '2']
# >>> list(product(x, y))
# # [('a', '1'), ('a', '2'), ('b', '1'), ('b', '2'), ('c', '1'), ('c', '2')]

# >>> list(product(y, repeat=3))
# # [('1', '1', '1'), ('1', '1', '2'), ('1', '2', '1'), ('1', '2', '2'), 
# # ('2', '1', '1'), ('2', '1', '2'), ('2', '2', '1'), ('2', '2', '2')]

# from itertools import product

# n = int(input())
# nums = list(range(1, n + 1))

# for i, j in product(nums, repeat=2):
#     if j == n:  
#         print(i * j)
#     else:
#         print(i * j, end=" ")

# for i in range(n):
#     step = 1
#     print(list(product(i, step)))

# from itertools import product

# n = int(input())

# names = ["А", "Б", "В"]
# nums = list(range(1, n + 1))

# print(*names)

# for i, j, k in product(nums, repeat=3):
#     if i + j + k == n: 
#         print(f"{i} {j} {k}")


# ввод : 5
# вывод
# А Б В
# 1 1 3
# 1 2 2
# 1 3 1
# 2 1 2
# 2 2 1
# 3 1 1

# n = input()
# a, b, c = int(n[0]), int(n[1]), int(n[2])

# minimum = min(a, b, c)
# maximum = max(a, b, c)
# middle = a + b + c - minimum - maximum  

# if minimum + maximum == middle * 2:
#     print("YES")
# else:
#     print("NO")


# a = int(input())
# b = int(input())
# c = int(input())

# if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
#     print("YES")
# else:
#     print("NO")


# Требуется поменять местами первый элемент массива с максимальным.

# Входные данные
# В первой строке вводится одно натуральное число, не превосходящее 
# 1000 – размер массива. Во второй строке задаются N чисел – элементы массива 
# (целые числа, не превосходящие по модулю 1000).

# n = int(input())
# nums = list(map(int, input().split()))

# greater = nums[0]

# for i in range(n):
#     ind = 0
#     if nums[i] > greater:
#         greater = nums[i]
#         ind = i
#     nums[ind] = nums[0]
#     nums[0] = greater

# print(*nums)

# Выходные данные
# Вывести получившийся массив. Если максимальных элементов несколько, требуется поменять первый из них.

# Примеры
# входные данные
# 5
# 1 2 3 4 5
# выходные данные
# 5 2 3 4 1