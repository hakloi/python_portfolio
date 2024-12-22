# num = int(input())

# lst = []

# while num != 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         while num % i == 0:
#             lst.append(i)
#             num //= i
#     if num > 1:
#         lst.append(num)
#         break
            
# print(*lst, sep=" * ")

# number = 500
# r = number // 2
# print(number)

# while (answer := input()) != "Угадал!":
#     if answer == "Меньше":
#         number -= r
#     if answer == "Больше":
#         number += r
        
#     if r >= 2:
#         r = (r + 1) //2 
#     print(number)