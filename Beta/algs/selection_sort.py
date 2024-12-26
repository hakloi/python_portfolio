def selectionSort(arr, n):
    for j in range(1, n):
        ins = arr[j]
        i = j - 1
        while (i >= 0 and ins < arr[i]):
            arr[i + 1] = arr[i]
            i -=1
        arr[i + 1] = ins
    return arr


arr = list(map(int, input().split()))
n = len(arr)
print(selectionSort(arr, n))