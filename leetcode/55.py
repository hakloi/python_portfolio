def solve(nums):
    reach = 0  
    for i, jump in enumerate(nums):
        if i > reach:  
            return False
        reach = max(reach, i + jump) 
        if reach >= len(nums) - 1: 
            return True
    return True 
        
        
nums = [3,2,1,0,4]
print(solve(nums))
    