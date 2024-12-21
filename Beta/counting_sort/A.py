def  CountSort(alist):
    count = [0] * 101
    
    res = []
    
    for i in alist:
        count[i] += 1
    
    index = 0
    for num in range(101):
        for _ in range(count[num]):
            alist[index] = num
            index += 1
            
    return alist

a = list(map(int, input().split()))
print(*CountSort(a))

# Входные данные
# 7 3 4 2 5
# Выходные данные
# 2 3 4 5 7