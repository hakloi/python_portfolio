import os
os.system('cls')

# s = set(input())
# print(''.join(s))

# s = input()
# w = input()

# res = set(s) & set(w)
# print(''.join(res))

# Продолжаем считать заек за окном поезда.

# Формат ввода
# В первой строке записано натуральное число 
# 𝑁
# N — количество выделенных придорожных местностей.
# В каждой из 
# 𝑁
# N последующих строк записано описание придорожной местности.

# Формат вывода
# Вывести все найденные объекты в придорожных местностях.
# n = int(input())
# all_set = set()

# for _ in range(n):
#     phrase = input().split()
#     all_set.update(phrase)
    
# print(*all_set, sep='\n')

# В первых двух строках указывается количество детей, любящих манную и овсяную каши (
# 𝑁
# N и 
# 𝑀
# M).
# Затем идут 
# 𝑁
# N строк — фамилии детей, которые любят манную кашу, и 
# 𝑀
# M строк с фамилиями детей, любящих овсяную кашу.
# Гарантируется, что в группе нет однофамильцев.

# Формат вывода
# Количество учеников, которые любят обе каши.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».

# m = int(input())
# o = int(input())

# m_set = set()
# o_set = set()

# for i in range(m):
#     surname = input()
#     m_set.add(surname)
    
# for j in range(o):
#     surname = input()
#     o_set.add(surname)
    
# res = list(m_set & o_set)
# if len(res) > 0:
#     print(len(res))
# else:
#     print('Таких нет')