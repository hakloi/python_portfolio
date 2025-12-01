from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = defaultdict(int)
unique = 0
left = 0
cur_sum = 0
min_sum = float('inf')

for right in range(n):
    val = a[right]
    cur_sum += val

    if 1 <= val <= k:
        if cnt[val] == 0:
            unique += 1
        cnt[val] += 1

    while unique == k:
        min_sum = min(min_sum, cur_sum)
        val_left = a[left]
        cur_sum -= val_left

        if 1 <= val_left <= k:
            cnt[val_left] -= 1
            if cnt[val_left] == 0:
                unique -= 1

        left += 1

print(min_sum)
