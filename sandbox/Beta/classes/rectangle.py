# n = int(input())
# m = int(input())

# max_len = len(str(n * m))

# current = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         current += 1
#         spaces = max_len - len(str(current))
#         print(f"{spaces*" "}{current}", end=" ")
#     print()

# n = int(input())
# m = int(input())

# max_val = n * m
# width = len(str(max_val))  

# for i in range(1, n + 1):
#     for j in range(m):
#         current = i + j * n
#         print(f"{current:>{width}}", end=" ")
#     print()

# n = int(input())
# m = int(input())

# max_val = n * m
# width = len(str(max_val))  

# current = 1
# for i in range(1, n + 1):
#     row = []
#     for j in range(m):
#         row.append(current)
#         current += 1
        
#     if i % 2 == 0:
#         row.reverse()
        
#     print(" ".join(f"{num:>{width}}" for num in row))

n = int(input())
m = int(input())

max_val = n * m
width = len(str(max_val))  

matrix = [[0] * m for _ in range(n)]

current = 1
for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            matrix[i][j] = current
            current += 1
    else:
        for i in range(n - 1, -1, -1):
            matrix[i][j] = current
            current += 1
            
for row in matrix:
    print(" ".join(f"{num:>{width}}" for num in row))