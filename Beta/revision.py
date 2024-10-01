import os
os.system('cls')

# a = int(input())
# b = int(input())
# c = int(input())

# res = float((b - a) / c)

# print(res)

# summa = int(input())
# last = input()


# print(int(last, 2) + summa)

# item = input()
# payment = int(input())

# print(payment - int(item, 2))


# Давайте приведём в порядок чек, который печатали ранее.
# Все строки должны быть длиной в 35 символов.

# Формат ввода
# Название товара;
# цена товара;
# вес товара;
# количество денег у пользователя.
# Формат вывода
# Красивый чек в формате:

# ================Чек================
# Товар:                    <продукт>
# Цена:     <число>кг * <число>руб/кг
# Итого:                   <число>руб
# Внесено:                 <число>руб
# Сдача:                   <число>руб
# ===================================

# item = input()
# price = int(input())
# weight = int(input())
# payment = int(input())

# total_cost = price * weight
# change = payment - total_cost

# # Вывод чека
# print(f"{'Чек':=^35}")
# print(f"Товар: {item:<27}")
# print(f"Цена:     {weight}кг * {price}руб/кг")
# print(f"Итого: {total_cost:>25}руб")
# print(f"Внесено: {payment:>23}руб")
# print(f"Сдача: {change:>25}руб")
# print("=" * 35)

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# s = list(map(int, input().split()))

# current_nod = s[0]
# for i in range(1, len(s)):
#     current_nod = gcd(current_nod, s[i])

# print(current_nod)

# ------------------------------------------------------
# lenght_title = int(input())
# n = int(input())
# text = ''
# count_n = 0

# for i in range(n):
#     phrase = input()
#     text += phrase
#     text += '\n'
#     count_n += 1
        
# if len(text) - count_n > lenght_title:
#     res = text[:lenght_title - 3] + '...'
# else:
#     res = text

# print(res)
# print(lenght_title, len(res))
# Формат вывода
# Сокращённый заголовок.

# Примечание
# Многоточие учитывается при подсчёте длины заголовка.
# Символ перевода строки при подсчёте длины не учитывается.

# Пример 1
# Ввод
# 144
# 5
# Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана
# Благодаря ей он может регулировать громкость,
# показывая расстояние между большим и указательным пальцами.
# Для этого ему понадобилась веб-камера, знания Python и
# библиотека для работы с компьютерным зрением.
# Вывод

# Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана
# Благодаря ей он может регулирова
# ------------------------------------------------------

# list_s = input().lower().split()

# res = ""
# for i in range(len(list_s)):
#     res += list_s[i]

# if res == res[::-1]:
#     print('YES')
# else:
#     print('NO')
# ------------------------------------------------------

# n = input()
# res_list = []
# res = ""
# counter = 1
# for i in range(len(n) - 1):
#     if n[i] == n[i + 1]:
#         counter += 1
#     else: 
#         res += n[i] + ' ' + str(counter) + '\n'
#         res_list.append(res)
#         counter = 1

# res += n[-1] + ' ' + str(counter)
# res_list.append(res)

# print(res)
# ------------------------------------------------------

# s = input().split()
# stack = []

# for el in s:
#     if el.isnumeric():
#         stack.append(int(el))
#     else:
#         if el in ['+', '-', '*', '/']:
            
#             if len(stack) < 2:
#                 break
#             op1 = stack.pop()
#             op2 = stack.pop()     
         
#             if el == '+':
#                 stack.append(op2 + op1)
#             elif el == '-':
#                 stack.append(op2 - op1)
#             elif el == '*':
#                 stack.append(op2 * op1)
#             elif el == '/':
#                 stack.append(op2 // op1)
            
#         elif el == '#':
#             if len(stack) < 1:
#                 break
#             op1 = stack[-1]
#             stack.append(op1)
            
#         elif el == "~":
#             if len(stack) < 1:
#                 break
#             op1 = (-1) * op1
#             stack.append(op1)
#         elif el == "!":
#             if len(stack) < 1:
#                 break
#             op1 = stack.pop()
#             factorial = 1
#             for i in range(1, op1 + 1):
#                 factorial *= i
#             stack.append(factorial)
            
#         elif el == "@":
#             if len(stack) < 3:
#                 break
#             op1 = stack.pop()
#             op2 = stack.pop()
#             op3 = stack.pop()
#             stack.append(op1)
#             stack.append(op2)
#             stack.append(op3)

# if len(stack) > 0:
#     print(stack.pop())


exp = input().split()

uno = ['~', '#', '!']
duo = ['+', '-', '*', '/']
trio = ['@']
operators = uno + duo + trio

stack = []

while exp != []:
    op = exp.pop(0)
    print(op)
    if op in uno:
        a = stack.pop()
        match op:
            case '~':
                stack.append(-a)
            case '!':
                res = 1
                for i in range(1, a + 1):
                    res *= i
                stack.append(res)
            case '#':
                stack.append(a)
                stack.append(a)
    elif op in duo:
        a = stack.pop()
        b = stack.pop()
        match op:
            case '+':
                stack.append(b + a)
            case '-':
                stack.append(b - a)
            case '*':
                stack.append(b * a)
            case '/':
                stack.append(b // a)
    elif op in trio:
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        match op:
            case '@':
                stack.append(b)
                stack.append(a)
                stack.append(c)
    else:
        stack.append(int(op))

print(int(stack[-1]))