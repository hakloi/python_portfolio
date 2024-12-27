def sort(arr, n):
    for j in range(1, n - 1):
        ins = arr[j]
        i = j -1
        while (i >= 0 and ins < arr[i]):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = ins
    
    return arr


arr = [5, 2, 7, 3, 4]
print(sort(arr, len(arr)))