nums = [-1,-100,3,99]
k = 2

n = len(nums)
k = k % n
rotated_arr = [0] * n

for i in range(n):
    rotated_arr[(k + i) % n] = nums[i]

for i in range(n):
    nums[i] = rotated_arr[i]

print(nums)
