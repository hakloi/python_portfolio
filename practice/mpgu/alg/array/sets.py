# n = int(input())
# m = int(input())

# res = (set([input() for _ in range(n)])).symmetric_difference(set([input() for _ in range(m)]))

# if res:
#     print(len(res))
# else:
#     print("Таких нет")

# ------------------------------
# n = int(input())
# m = int(input())

# list1 = set()
# list2 = set()

# for _ in range(n + m):
#     name = input()
#     if name in list1:
#         list2.add(name)
#     else:
#         list1.add(name)

# print(list1, list2)

# if len(junction := (list1 ^ list2)) != 0:
#     print(junction)
#     print(len(junction))
# else:
#     print('Таких нет')

# ----------------------------
# n = int(input())
# m = int(input())

# list1 = set()
# list2 = set()

# for _ in range(n + m):
#     name = input()
#     if name in list1:
#         list2.add(name)
#     else:
#         list1.add(name)


# junction = list1 ^ list2
# # print(junction)
# if len(junction) != 0:
#     junction = list(junction)
#     junction.sort()
#     print(*junction, sep='\n')
# else:
#     print('Таких нет')
    
# 3
# 2
# Васильев
# Петров
# Васечкин
# Иванов
# Михайлов

# Вывод
# Васечкин
# Васильев
# Иванов
# Михайлов
# Петров
# Пример 2

# Ввод
# 3
# 3
# Иванов
# Петров
# Васечкин
# Иванов
# Петров
# Васечкин
# Вывод

# Таких нет

# ---------------------------
# Каждый из N
#  школьников некоторой школы знает Mi
#  языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

# Входные данные
# Первая строка входных данных содержит количество школьников N
# . Далее идет N
#  чисел Mi
# , после каждого из чисел идет Mi
#  строк, содержащих названия языков, которые знает i
# -й школьник. Длина названий языков не превышает 1000 символов, количество различных языков не более 1000. 1≤N≤1000
# , 1≤Mi≤500
# .
kids = int(input())
langs = int(input())


for i in range(kids):
    print(f"kid {i}:")
    for j in range(langs):
        idioma = input()
    

# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники. Начиная со 
# второй строки - список таких языков. Затем - количество языков, которые знает хотя бы 
# один школьник, на следующих строках - список таких языков.

# Примеры
# входные данные
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English
# выходные данные
# 1
# English
# 3
# Russian
# Japanese
# English