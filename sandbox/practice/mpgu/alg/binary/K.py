n, k = map(int, input().split())

l = 0
r = n * 100

while r - l > 1:
    m = (l + r) // 2
    cur = k
    cnt = 0
    while cur <= m:
        cnt += m // cur - m // (cur * k)
        cur *= k ** 2
    if cnt >= n:
        r = m
    else: 
        l = m
        
print(r)