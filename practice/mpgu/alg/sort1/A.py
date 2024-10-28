n = int(input())
nums = list(map(int, input().split()))

ind = 0
for i in range(1, n):
    if nums[i] > nums[ind]:
        ind = i

nums[0], nums[ind] = nums[ind], nums[0]

print(*nums)