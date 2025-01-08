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

n = int(input())
current_number = 1
res = []

for i in range(1, n + 1):
    arr = []
    for j in range(i):
        if current_number > n:
            break
        arr.append(current_number)
        current_number += 1
    line = " ".join(str(el) for el in arr)
    res.append(line)
    
    if current_number > n:
        break
    

max_width = len(res[-1])
for line in res:
    print(f"{line:^{max_width}}")