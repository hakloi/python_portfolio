def  CountSort(alist, ln):
    offset = 10000
    count = [0] * (2 * offset + 1)
    
    for i in alist:
        count[i + offset] += 1
    
    index = 0
    for num in range(-offset, offset + 1):
        for _ in range(count[num + offset]):
            alist[index] = num
            index += 1
            
    return alist

n = int(input())
a = list(map(int, input().split()))
print(*CountSort(a, n))