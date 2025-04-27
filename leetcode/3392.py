nums = [1,2,1,4,1]

cnt = 0
for a, b, c in zip(nums, nums[1:], nums[2:]):
    if (a + c) * 2 == b:
        cnt += 1
print(cnt)
        
