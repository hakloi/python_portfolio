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

def split_numbers(s):
    new = tuple(map(int, s.split()))
    return new

result = split_numbers("1 2 3 4 5")
print(result)