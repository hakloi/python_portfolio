def mySqrt(self, x):
    left = 0
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        
        res = mid * mid 
        if res == x:
            return mid
        if res > x:
            right = mid - 1
        else: 
            left = mid + 1 
            
    return right