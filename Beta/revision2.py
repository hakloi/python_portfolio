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