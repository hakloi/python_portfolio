from collections import deque

def containsNearbyDuplicate(nums, k):
    window = deque()
    
    for i, num in enumerate(nums):
        print(i, num)
        if num in window:
            return True
        
        window.append(num)
        
        if len(window) > k:
            window.popleft()
    
    return False


nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))