def x(arr, low, high):
    elem = arr[high]
    i = low
    for j in range(i, high):
        if arr[j] <= elem:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[high], arr[i] = arr[i], arr[high]
    return i
    
    
arr = [5, 2, 7, 3, 4]
print(x(arr, 0, len(arr)-1))

print(16 % 4)