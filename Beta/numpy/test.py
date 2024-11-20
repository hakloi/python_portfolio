import numpy as np

def multiplication_matrix(n):
    res = []
    for i in range(1, n + 1):
        arr = np.arange(1, n + 1) * i
        res.append(arr)
    return np.array(res)
        
        
print(multiplication_matrix(3))


# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]