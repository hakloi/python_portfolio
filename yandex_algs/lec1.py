# s = input()

# counter = {}
# max_char = None
# max_value = 0

# for char in s:
#     if char.isalpha():
#         counter[char] = counter.get(char, 0) + 1
        
#         if counter[char] > max_value:
#             max_value = counter[char]
#             max_char = char

# print(max_char)
import math

a = int(input())
b = int(input())
c = int(input())

x = []

def roots(a, b, c):
    if a != 0:
        if b != 0 and c != 0:
            discr = b ** 2 - 4 * a * c
            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / 2 * a
                x2 = (-b - math.sqrt(discr)) / 2 * a
                x.append(x1)
                x.append(x2)
            elif discr == 0:
                x.append(-b / (2 * a))
            else:
                print('Нет корней')
        elif b != 0 and c == 0:
            
            
            
            
        
        
print(roots(a, b, c))