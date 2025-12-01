def bubbleSort(arr, n):
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        n -= 1
    return arr


arr = list(map(int, input().split()))
n = len(arr)
print(bubbleSort(arr, n))