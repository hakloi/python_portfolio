n, r, c = map(int, input().split())
a = sorted(int(input()) for _ in range(n))
left = -1
right = a[-1] - a[0] 

while right - left > 1:
    m = (left + right) // 2
    cnt = 0
    i = 0
    while (i + c <= n):
        if a[i + c - 1] - a[i] <= m:
            cnt += 1
            i += c
        else:
            i += 1
            
    if cnt >= r:
        right = m
    else:
        left = m

print(right)

# 8 2 3
# 170
# 205
# 225
# 190
# 260
# 130
# 225
# 160