def climbStairs(n):
        if n <= 3: return n
        
        prev1 = 2
        prev2 = 3
        cur = 0
        
        for _ in range(3, n):
            cur = prev1 + prev2 
            prev1 = prev2
            prev2 = cur
            
        return cur
            
    
print(climbStairs(6))