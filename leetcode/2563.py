import bisect

def countFairPairs(nums, lower, upper):
    # pairs = []
    
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         summa = nums[i] + nums[j]
    #         if summa >= lower and summa <= upper:
    #             pairs.append((i, j))
    # return pairs
    nums.sort()
    n = len(nums)
    cnt = 0
    
    for i in range(n):
        left = bisect.bisect_left(nums, lower - nums[i], i + 1)
        right = bisect.bisect_right(nums, upper - nums[i], i + 1)
        cnt += right - left
        
    return cnt

print(countFairPairs([0,1,7,4,4,5], 3, 6))
print(countFairPairs([1,7,9,2,5], 11, 11))