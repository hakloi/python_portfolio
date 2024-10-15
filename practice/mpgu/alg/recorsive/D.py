def c(n, k):
    if k == 0 or k == n:
        return 1
    return c(n - 1, k -1) + c(n - 1, k)
    
n = int(input())
k = int(input())

print(c(n, k))