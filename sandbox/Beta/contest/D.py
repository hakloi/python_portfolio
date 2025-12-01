import math

A, B, C, D = map(int, input().split())
count = 0

max_w = int(math.isqrt(B))

for w in range(1, max_w + 1):
    h_min1 = (A + w - 1) // w
    h_max1 = B // w

    h_min2 = max((C + 1) // 2 - w, 1)
    h_max2 = (D // 2) - w

    h_min = max(h_min1, h_min2, w)
    h_max = min(h_max1, h_max2)

    if h_min <= h_max:
        count += h_max - h_min + 1

print(count)
