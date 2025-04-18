def isHappy(n):
    seen = set()
    
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        
        n = sum(int(el) ** 2 for el in str(n))
    
    return True

print(isHappy(2))