def selectionSort(arr, n):
    for i in range(0, n - 1):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
        
    return arr

arr = list(map(int, input().split()))
n = len(arr)
print(selectionSort(arr, n))