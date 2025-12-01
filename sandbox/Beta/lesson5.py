# Вложенные циклы 
import os
os.system('cls')

# for i in range(1,6):
#     for j in range(-2,0):
#         print(i, j)

# while input("Введи 'НЕТ': ") != "НЕТ":
#     pass
# else: 
#     print("Завершен.")

# while (text := input("Введи 'НЕТ':")) != 'НЕТ':
#     if text == 'Beta':
#         break
# else:
#     print("Завершен.")

# The multiplication table
# n = int(input())

# for i in range(n):
#     for j in range(n):
#         print((i + 1) * (j + 1), end=' ')
#     print()

# The multiplication table
# n = int(input())

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(f'{j} * {i} = {i*j}')


# n = int(input())
 
# num = 1
# count = 0
# for i in range(1, n+1):
#     for j in range(i):
#         if count < n:
#             print(num, end=" ")
#             num += 1
#             count += 1
#     print()

# n = int(input())
# summ = 0

# for i in range(n):
#     el = input()
#     for e in el:
#         summ += int(e)
# print(summ)
    
# n = int(input())
# count = 0

# for i in range(n):
#     z = 0
#     while (s := input()) != 'ВСЁ': 
#         if s == "зайка":
#             z += 1
#     if z > 0:
#         count += 1
#         z = 0
# print(count)