# 1 3 4 7 9
# 2 3 7 10 11
def Intersection(A, B):
    i, j = 0, 0
    res = []
    
    while i < len(A) and j < len(B):
        if (A[i] == B[j]):
            res.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else: 
            j += 1
        
    return res


    
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(*Intersection(arr1, arr2))