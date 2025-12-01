import numpy as np

def rotate(arr, angle):
    k = angle // 90
    return np.rot90(arr, -k)

print(np.arange(12).reshape(3, 4))
print(rotate(np.arange(12).reshape(3, 4), 90))

print(rotate(np.arange(12).reshape(3, 4), 270))