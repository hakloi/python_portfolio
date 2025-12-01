L = int(input())
N = int(input())
road = [int(input()) for _ in range(N)]

fix = [i for i, v in enumerate(road) if v == 1]

workers = 0
i = 0
while i < len(fix):
    start = fix[i]
    end = start + L - 1
    workers += 1
    
    while i < len(fix) and fix[i] <= end:
        i += 1
        
print(workers)
# 3
# 8
# 0
# 0
# 1
# 0
# 1
# 0
# 1
# 0