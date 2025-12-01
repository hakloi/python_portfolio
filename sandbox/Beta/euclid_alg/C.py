def factorial_sum(a1, b1, a2, b2):
    if b1 != b2:
        b = b1 * b2
        a = (a1 * b2) + (a2 * b1)
    else:
        a = a1 + a2
        b = b1
    
    n1, n2 = a, b
    while b != 0:
        a, b = b, a % b
    
    return n1 // a, n2 // a
        
        
        

a1, b1, a2, b2 = map(int, input().split())
# a, b = a1 + a2, b1 + b2
print(*factorial_sum(a1, b1, a2, b2))