def isZeroArray(nums, queries):
    n = len(nums)
    
    cnt = [0] * (n + 1)
    
    for l, r in queries:
        cnt[l] += 1
        if r + 1 < len(cnt):
            cnt[r + 1] -= 1
   
    for i in range(n):
        cnt[i] += cnt[i - 1]

    for j in range(len(nums)):
        if nums[j] > cnt[j]:
            return False
            
    return True



# print(isZeroArray([1,0,1], [[0,2]]))
# print(isZeroArray([4,3,2,1], [[1,3],[0,2]]))
print(isZeroArray([2, 1, 1, 1, 2], [(1, 3)]))
       