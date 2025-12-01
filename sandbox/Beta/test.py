import os
os.system('cls')

# import math

# # ctrl + / (slash)
# # name = 'Viola'
# name_student = "Beta"
# n = 10.4

# print(math.pi)

# n = int(input())
# count = 4
# for i in range(count, 0, -1):
#     print(f'До старта {i} секунд(ы)')
#     for j in range(1,n):
#         print(f'Старт {j}!!!')
#     count += 1
    
# n = int(input())
# count = 3
# for i in range(n+1):
#     if i > 0:
#         print(f'Старт {i}!!!')
#     if i < n:
#         for j in range(count, 0, -1):
#             print(f'До старта {j} секунд(ы)')
#     count += 1

# count = int(input())
# res_name = ''
# res_n = 0
# for i in range(count):
#     name = input()
#     n = int(input())
#     summ = 0
#     while n > 0:
#         summ += n % 10
#         n //= 10
#     if summ >= res_n:
#         res_n = summ
#         res_name = name
# print(res_name)

# count = int(input())
# flag = 'YES'
# for i in range(count):
#     word = input()
#     if (word[0] not in 'абв'):
#         flag = 'NO'
        
# print(flag)

# n = int(input())
# res = ''

# for i in range(n):
#     num = input()
#     great = 0
#     for el in num:
#         if int(el) > great:
#             great = int(el)
#     res += str(great)
    
# print(res)

# n = int(input())

# print("A B C")
# for i in range(1,n-1):
#     for j in range(1, n-1):
#         k = n-i-j
#         if k > 0:
#             print(i, j, k)


# n = int(input())
# count_primes = 0 

# for i in range(n):
#     num = int(input())
    
#     is_prime = True
#     if num <= 1:
#         is_prime = False
#     else:
#         for j in range(2,  int(num ** 0.5) + 1):
#             if (num % j == 0):
#                 is_prime = False
#                 break
#     if is_prime == True:
#         count_primes += 1
# print(count_primes)
import json

f1 = input()
f2 = input()

with open(f1, "r", encoding="utf-8") as filein:
        nums = []
        for line in filein:
            nums.extend(map(int, line.split()))
        
        cnt = len(nums)
        pos = len(list(x for x in nums if x > 0))
        min_v = min(nums)
        max_v = max(nums)
        summa = sum(nums)
        avg = summa / cnt
        
        records = {"count": cnt,
                "positive_count": pos,
                "min": min_v,
                "max": max_v,
                "sum": summa,
                "average": f"{avg:.2f}"}


with open(f2, "w", encoding="utf-8") as fileout:
        json.dump(records, fileout, ensure_ascii=False, indent=4) 
# numbers.txt
# statistics.json