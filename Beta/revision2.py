# a = input()
# b = input()
# c = input()

# if a[0] in b and a[0] in c:
#     print(a[0])
# elif a[1] in b and a[1] in c:
#     print(a[1])

# a = input()
# lst = [int(char) for char in a]
# res = []


# small = lst[0]
# big = lst[0]
# for i in range(len(lst)):
#     if lst[i] < small and lst[i] != 0:
#         small = lst[i]
#     if lst[i] > big:
#         big = lst[i]
#     lst.remove(small)
#     lst.remove(big)

# fst = str(small) + str(lst[0]) 
# res.append(fst)
# lst = str(big) + str(lst[0])
# res.append(lst)

# print(*res) 
        
        
# a = input()
# small = ''
# big = ''

# if a[0] < a[1] and a[0] < a[2] and a[0] != '0':
#     small = a[0]
# elif a[1] < a[0] and a[1] < a[2] and a[1] != '0':
#     small = a[1]
# else:
#     small = a[2]
    
# print(small)

# new = a.replace(small, "")

# if a[0] > a[1]:
#     big = a[0]
# else:
#     big = a[1]
    
# mid = new.replace(big, "")
    
# print(small + mid, big + mid)

# a = int(input())

# n1 = a // 100
# n2 = a % 10
# n3 = a // 10 % 10

# small = min(n1, n2, n3)
# big = max(n1, n2, n3)

# if small != 
# print(small, big)
    
# a = input()

# digits = [int(d) for d in a]
# digits_no_zero = [d for d in digits if d != 0]
# small = min(digits_no_zero)
# big = max(digits)

# mid_candidates = [d for d in digits if d != small and d != big]

# mid = mid_candidates[0] if mid_candidates else small  

# print(f"{small}{mid} {big}{mid}")

# a = int(input())
# b = int(input())

# first = a // 10
# second = a % 10
# third = b // 10
# forth = b % 10

# if first > second:
#     first, second = second, first
# if first > third:
#     first, third = third, first
# if first > forth:
#     first, forth = forth, first

# if second > third:
#     second, third = third, second
# if second > forth:
#     second, forth = forth, second

# if third > forth:
#     third, forth = forth, third

# print(f"{forth}{(second + third) % 10}{first}")

# p = int(input())
# v = int(input())
# t = int(input())
# fst = p

# if p > v and p > t:
#     print(f"{'Петя':^24}") 
#     if v > t:
#         print(f"{'Вася':^8}") 
#         print(f"{'Толя':>22}") 
#     if t > v:
#         print(f"{'Толя':^8}") 
#         print(f"{'Вася':>22}") 
        
# elif v > p and v > t:
#     print(f"{'Вася':^24}") 
#     if t > p:
#         print(f"{'Толя':^8}") 
#         print(f"{'Петя':>22}") 
#     if p > t:
#         print(f"{'Петя':^8}") 
#         print(f"{'Толя':>22}") 
    
# elif t > p and t > v:
#     print(f"{'Толя':^24}") 
#     if v > p:
#         print(f"{'Вася':^8}") 
#         print(f"{'Петя':>22}") 
#     if p > v:
#         print(f"{'Петя':^8}") 
#         print(f"{'Вася':>22}") 
    
# print(f"{'II':^8}", end="")
# print(f"{'I':^8}", end="")
# print(f"{'III':^8}", end="")
#           Петя          
#   Толя  
#                   Вася  
#    II      I      III  
import math 

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else: 
            print("No solution")
    else: 
        x = -c / b
        print(f"{x:.2f}")
else:
    dis = b * b - 4 * a * c
    if dis > 0:
        x1 = (-b - math.sqrt(dis)) / (2 * a)
        x2 = (-b + math.sqrt(dis)) / (2 * a)
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
    if dis == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        print("No solution")