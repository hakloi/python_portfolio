# size = int(input())
# width = int(input())
# size = 5
# width = 5

#  1 | 2 | 3 
# -----------
#  2 | 4 | 6 
# -----------
#  3 | 6 | 9 

# size = int(input())
# width = int(input())

# for i in range(1, size + 1):
#     row = [f"{i * j:^{width}}" for j in range(1, size + 1)]
#     print("|".join(row))
    
#     if i < size:
#         print('-' * (size * width + (size - 1)))


# n = int(input())

# cnt = 0
# for _ in range(n):
#     num = input()
    
#     if num == num[::-1]:
#         cnt +=1
        
# print(cnt)

# n = int(input())
# current_number = 1
# res = []

# for i in range(1, n + 1):
#     arr = []
#     for j in range(i):
#         if current_number > n:
#             break
#         arr.append(current_number)
#         current_number += 1
#     line = " ".join(str(el) for el in arr)
#     res.append(line)
    
#     if current_number > n:
#         break
    

# max_width = len(res[-1])
# for line in res:
#     print(f"{line:^{max_width}}")


# n = int(input())
# matrix = [[0] * n for _ in range(n)]

# for layer in range((n + 1) // 2):
#     num = layer + 1
    
    
# n = int(input())

# matrix = [[0] * n for _ in range(n)]

# for layer in range((n + 1) // 2):
#     num = layer + 1
    
#     for i in range(layer, n - layer):
#         matrix[layer][i] = num
        
#     for i in range(layer + 1, n - layer):
#         matrix[i][n - layer] = num
        
#     for i in range(layer + 1, n - layer):
#         matrix[n - layer - 1][n - i - 1] = num

#     for i in range(layer + 1, n - layer - 1):
#             matrix[n - i - 1][layer] = num
            
# for row in matrix:
#     print(" ".join(str(el) for el in row))


# num = int(input())
# res = {}

# for i in range(2, 11):
#     rem = []
#     n = num
#     while n != 0:
#         if n % i != 0:
#             rem.append(n % i)
#         else:
#             rem.append(0)
#         n = n // i 
#     res[i] = sum(rem)

# max_base = max(res, key=res.get)

# print(max_base)
            
            
# lst = [1, 3, 5, 3, 2]

# sorted(lst)
# print(lst)

# lst.sort()
# print(lst)


# treasures = dict()

# for _ in range(count := int(input())):
#     x, y = input().split()
#     index = (int(x) // 10, int(y) // 10)
#     treasures[index] = treasures.get(index, 0) + 1

# print(max(treasures.values()))

toys = []
unique = {}

for _ in range(int(input())):
    name, str = input().split(': ')
    toys.extend(set(str.split(', '))) 
    
for toy in sorted(toys):
    unique[toy] = unique.get(toy, 0) + 1
    
for toy in unique:
    if unique[toy] == 1:
        print(toy)
    