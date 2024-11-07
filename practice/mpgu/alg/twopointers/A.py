def merge(A, B):
    i, j = 0, 0
    res = []
    
    while i < len(arr1) and j < len(arr2):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    
    while i < len(A):
        res.append(A[i])
        i += 1
    
    while j < len(B):
        res.append(B[j])
        j += 1
        
    return res


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(*merge(arr1, arr2))

# 1 5 7
# 2 4 4 5