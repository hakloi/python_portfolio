def nod(a, b):
    n1 = a
    n2 = b
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    
    return a // n1, b // n1

a, b = map(int, input().split())
print(*nod(a, b))