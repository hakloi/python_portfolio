# def number_length(n):
#     s = "".join(el for el in str(n) if el.isnumeric())
#     return len(s)


# result = number_length(-100500)
# print(result)


# def month(n, lan):
#     en_dct = {1: "January",
#               2: "February",
#               3: "March",
#               4: "April",
#               5: "May",
#               6: "June",
#               7: "July",
#               8: "August",
#               9: "September",
#               10: "October",
#               11: "November",
#               12: "December",
#               }
    
#     ru_dct = {1: "Январь",
#               2: "Февраль",
#               3: "Март",
#               4: "Апрель",
#               5: "Май",
#               6: "Июнь",
#               7: "Июль",
#               8: "Август",
#               9: "Сентябрь",
#               10: "Октябрь",
#               11: "Ноябрь",
#               12: "Декабрь",
#               }
#     if lan == "ru":
#         for k, v in ru_dct.items():
#             if k == n:
#                 return v
            
#     if lan == "en":
#         for k, v in en_dct.items():
#             if k == n:
#                 return v       

# result1 = month(1, "en")
# result2 = month(3, "ru")
# print(result1, result2)

# def split_numbers(s):
#     new = tuple(map(int, s.split()))
#     return new

# result = split_numbers("1 2 3 4 5")
# print(result)


# lst = []

# def modern_print(s):
#     global lst
#     if s not in lst:
#         lst.append(s)
#         return s


# modern_print("Hello!")
# modern_print("Hello!")
# modern_print("How do you do?")
# modern_print("Hello!")

# def can_eat(horse, figure):
#     x, y = horse
#     x1, y1 = figure
    
#     if abs(x - x1) == 1 and abs(y - y1) == 2:
#         return True
#     elif abs(x - x1) == 2 and abs(y - y1) == 1:
#         return True
#     else: return False


# result = can_eat((5, 5), (6, 6))
# print(result)

# def is_palindrome(s):
#     if isinstance(s, list | tuple):
#         if s[::] == s[::-1]:
#             return True
#         else: 
#             return False
    
#     elif isinstance(s, str):
#         s = s.lower().replace(" ", "")
#         if s[::] == s[::-1]:
#             return True
#         else: 
#             return False
    
#     elif isinstance(s, int):
#         s = str(s)
#         if s[::] == s[::-1]:
#             return True
#         else: 
#             return False
        
        

# result3 = is_palindrome(123)
# print(result3)

# def is_prime(num):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
        
#     return True
        
# result = is_prime(79701)
# print(result)

# def merge(t1, t2):
#     res = ()
#     i, j = 0, 0
    
#     while i < len(t1) and j < len(t2):
#         if t1[i] < t2[j]:
#             res += (t1[i],)
#             i += 1
#         else:
#             res += (t2[j],)
#             j += 1
            
#     while i < len(t1):
#         res += (t1[i],)
#         i += 1
        
#     while j < len(t2):
#         res += (t2[j],)
#         j += 1
        
#     return res
    
# result = merge((7, 12), (1, 9, 50))
# print(result)

#14 6 -> 6 != 0 -> a=6, b = 14 % 6 = 2;
# 2 != 0; a = 2, b = 6 %2 = 3

def gcd(a, b): 
    while b != 0: 
        a, b = b, a % b
    return a

n = int(input())
lst = [int(input()) for _ in range(n)]

result = lst[0]
for num in lst[1:]:
    result = gcd(result, num)
    
print(result)





    
    
# 2
# 12
# 42