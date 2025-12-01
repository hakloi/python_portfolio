n = int(input())
m = int(input())
t = int(input())

left, right = 0, min(n, m) // 2
answer = 0

while left <= right:
    mid = (left + right) // 2
    tiles_needed = n * m - (n - 2 * mid) * (m - 2 * mid)
    
    if tiles_needed <= t:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
