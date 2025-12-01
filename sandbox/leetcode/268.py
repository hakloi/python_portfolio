def missingNumber(nums):
    nums.sort()
    l, r = 0, len(nums)
    
    while l < r:
        mid = (l + r) // 2
        if mid < len(nums) and nums[mid]:
            r = mid
        else:
            l = mid + 1

    return l

nums = [3,0,1]
print(missingNumber(nums))