import numpy as np

def stairs(arr):
    n = len(arr)
    return np.array([np.roll(arr, i) for i in range(n)])
    
    
print(stairs(np.arange(3)))
# [[0 1 2]
#  [2 0 1]
#  [1 2 0]]
print(stairs(np.arange(5)))
# [[0 1 2 3 4]
#  [4 0 1 2 3]
#  [3 4 0 1 2]
#  [2 3 4 0 1]
#  [1 2 3 4 0]]