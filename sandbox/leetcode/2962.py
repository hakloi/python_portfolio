def subArrays(nums, k):
    max_num = max(nums)
    res = 0
    l = 0
    cnt = 0
    
    for r in range(len(nums)):
        if nums[r] == max_num:
            cnt += 1

        while cnt >= k:
            if nums[l] == max_num:
                cnt -= 1
            l += 1
            
        res += l
            
    return res


nums = [1,3,2,3,3]
k = 2
print(subArrays(nums, k))


# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: 
#     [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].