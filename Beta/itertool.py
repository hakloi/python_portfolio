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

import itertools

m = input().split(", ")
p = input().split(", ")
d = input().split(", ")

res = itertools.chain(m, p, d)
for i, v in enumerate(sorted(list(res)), 1):
    print(f"{i}. {v}")