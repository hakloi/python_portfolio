# def get_num(num):
#     res = ""
#     for char in num:
#         if char == "-" or char.isnumeric():
#             res += char
#     return int(res)


# a = input()
# b = input()

# res = [x ** 2 for x in range(get_num(a), get_num(b) + 1)]
# print(res)


# a = 1
# b = 5

# Список квадратов

# Большинство задач этой главы ориентированы на отработку навыков по построению списочных выражений.

# Вашему решению будет предоставлены две переменные a и b. Напишите списочное выражение для получения 
# квадратов чисел из диапазона [a,b].

# Примечание
# В решении не должно быть ничего, кроме списочного выражения.

# [x ** 2 for x in range(a, b + 1)]

# Пример 1
# Ввод
# a = 1
# b = 5
# Вывод
# [1, 4, 9, 16, 25]

# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
# n = int(input())
# res = [[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]
# print(res)

# sentence = 'Мама мыла раму'
# # [4, 4, 4]
# res = [len(x) for x in sentence.split()]
# print(res)

# numbers = [1, 2, 3, 4, 5]
# # {1, 3, 5}
# res = {x for x in numbers if x % 2 != 0}
# print(res)

# Полным квадратом назовём натуральное число, которое является квадратом другого натурального числа. 
# Например: 1, 25, 144.

# Вашему решению будет предоставлен список numbers, содержащий натуральные числа.

# Разработайте выражение для генерации множества всех чисел, которые выступают полными квадратами.

# Примечание
# В решении не должно быть ничего, кроме выражения.

# import math

# numbers = [1, 2, 3, 4, 5]

# res = {x for x in numbers if x ** (0.5) % 1 == 0}
# print(res)

# text = 'Мама мыла раму!'
# d = {char: text.lower().count(char) for char in text.lower() if char.isalpha()}
# # d = {}

# # for char in text:
# #     if char.isalpha():
# #         if char in d:
# #             d[char] += 1
# #         else:
# #             d[char] = 1
            
# print(d)


# res = {x for x in }

# {'а': 4, 'л': 1, 'м': 4, 'р': 1, 'у': 1, 'ы': 1}


# numbers = {15, 49, 36}
# res = {num: [i for i in range(1, num + 1) if num % i == 0] for num in numbers}
# print(res)
# {15: [1, 3, 5, 15], 36: [1, 2, 3, 4, 6, 9, 12, 18, 36], 49: [1, 7, 49]}

# string = 'Российская Федерация'
# abr = ''.join([x[0] for x in string.upper().split()])
# print(abr)

# 'РФ'


# numbers = [3, 1, 2, 3, 2, 2, 1]

# res = '-'.join((str(num) for num in sorted(set(numbers))))
# print(res)
    
# '1 - 2 - 3'


# rle = [('a', 2), ('b', 3), ('c', 1)]
# res = ''.join(str(w) * f for w, f in rle)
# print(res)
# 'aabbbc'


# n = int(input())
# frequency = {}

# for i in range(n):
#     surname = input()
#     frequency[surname] = frequency.get(surname, 0) + 1

# summa = sum(v for v in frequency.values() if v > 1)

# print(summa)

# n = int(input())
# frequency = {}

# for i in range(n):
#     surname = input()
#     frequency[surname] = frequency.get(surname, 0) + 1
    
# namesake = {k: v for k, v in frequency.items() if v > 1}

# if namesake:
#     for k, v in sorted(namesake.items()):
#         print(f"{k} - {v}")
# else:
#     print("Однофамильцев нет")
        
# n = int(input())
# meals = {input(): 0 for _ in range(n)}

# m = int(input())
# for i in range(m):
#     amount = int(input())
#     for j in range(amount):
#         meal = input()
#         if meal in meals.keys():
#             meals[meal] += 1

# res = [k for k, v in meals.items() if v == 0]
# res.sort()
# print(*res, sep="\n")

# done = []
# for j in range(m):
    
# 5
# Овсянка
# Рис
# Суп
# Манная каша
# Рыба
# 2
# 3
# Рис
# Суп
# Рыба
# 2
# Рис
# Рыба

# --------------------------------


# n = int(input()) #4
# goods = [input() for _ in range(n)] #

# recipies = {}
# m = int(input()) #3
# for _ in range(m):
#     dish = input() #тосты
#     prod_num = int(input()) #2
#     prods = [input() for _ in range(prod_num)]
#     recipies[dish] = prods

# possible_dishes = []
# for dish, prods in recipies.items():
#     if all(prod in goods for prod in prods):  
#         possible_dishes.append(dish)
    
# if possible_dishes:
#     possible_dishes.sort()
#     print(*possible_dishes, sep="\n")
# else:
#     print("Готовить нечего")

# 4
# Яблоки
# Хлеб
# Варенье
# Картошка
# 3
# Тосты
# 2
# Хлеб
# Варенье
# Яблочный Сок
# 1
# Яблоки
# Яичница
# 1
# Яйца
# def trans_bin(nums):
#     res_list = []
#     for num in nums:
#         term = bin(num)
#         res_list.append(term[2:])
#     return res_list


# numbers = list(map(int, input().split()))
# nums = trans_bin(numbers)
# done = []

# for num in nums:
#     dictionary = {}
#     dictionary["digits"] = len(num)
#     dictionary["units"] = num.count("1")
#     dictionary["zeroes"] = num.count("0")
#     done.append(dictionary)

# print(done)
#  {
#         "digits": 3,
#         "units": 2,
#         "zeros": 1
#     },


# 5 8 12


# def trans_bin(nums):
#     return [bin(num)[2:] for num in nums] 

# numbers = list(map(int, input().split()))  

# done = [{"digits": len(num), "units": num.count("1"), "zeros": num.count("0")} for num in trans_bin(numbers)]

# print(done)

# seen = set()

# while (phrase := input()) != '':
#     animals = phrase.split()
#     for i in range(len(animals)):
#         if animals[i] == "зайка":
#             if i > 0:
#                 seen.add(animals[i - 1])
#             if i < len(animals) - 1:
#                 seen.add(animals[i + 1])

# seen = list(seen)
# seen.sort()
# print(*seen, sep="\n")


# березка елочка зайка волк березка
# сосна зайка сосна елочка зайка медведь
# сосна сосна сосна белочка сосна белочка

# волк
# елочка
# медведь
# сосна