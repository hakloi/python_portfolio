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