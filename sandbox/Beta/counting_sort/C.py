def  CountSort(lst):
    min_el = min(lst)
    max_el = max(lst)
    
    range_size = max_el - min_el + 1
    
    count = [0] * range_size
    
    for num in lst:
        count[num - min_el] += 1
        
    index = 0
    for num in range(range_size):
        while count[num] > 0:
            lst[index] = num + min_el
            index += 1
            count[num] -= 1
            
    return lst

n = int(input())
lst = list(map(int, input().split()))
print(*CountSort(lst))