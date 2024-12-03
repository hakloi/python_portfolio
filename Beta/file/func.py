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

def is_palindrome(s):
    if isinstance(s, list | tuple):
        if s[::] == s[::-1]:
            return True
        else: 
            return False
    
    elif isinstance(s, str):
        s = s.lower().replace(" ", "")
        if s[::] == s[::-1]:
            return True
        else: 
            return False
    
    elif isinstance(s, int):
        s = str(s)
        if s[::] == s[::-1]:
            return True
        else: 
            return False
        
        

result3 = is_palindrome(123)
print(result3)