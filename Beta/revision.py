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

item = input()
price = int(input())
weight = int(input())
payment = int(input())

total_cost = price * weight
change = payment - total_cost

# Вывод чека
print(f"{'Чек':=^35}")
print(f"Товар: {item:<27}")
print(f"Цена:     {weight}кг * {price}руб/кг")
print(f"Итого: {total_cost:>25}руб")
print(f"Внесено: {payment:>23}руб")
print(f"Сдача: {change:>25}руб")
print("=" * 35)
