def func(nums):
    if not nums:
        return []
    
    res = []
    start = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if nums[i - 1] == start:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i - 1]}")
            start = nums[i]
        
    if start != nums[-1]:
        res.append(f"{start}->{nums[-1]}")
    else:
        res.append(str(start))
        
    return res

nums = [0,1,2,4,5,7]
print(func(nums))

# ["0->2","4->5","7"]