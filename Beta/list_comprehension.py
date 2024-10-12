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

n = int(input())
frequency = {}

for i in range(n):
    surname = input()
    frequency[surname] = frequency.get(surname, 0) + 1

for k, v in frequency.items():
    if v > 1:
        print(f"{k} - {v}")