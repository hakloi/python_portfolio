from collections import deque

def slidingWindowMin(n, k, nums):
    d = deque() 
    min_lst = []
    
    for i in range(n):
        # проверка переполности дека
        if d and d[0] < i - k + 1:
            d.popleft()
        
        # если конец деки больше нынешнего эл, то мы ставим нынеш элемент в конец
        # и удаляем изначальный конец деки
        while d and nums[d[-1]] >= nums[i]:
            d.pop()
        
        # добавляем в деку
        d.append(i)
        
        # если окно полное
        if i >= k - 1:
            min_lst.append(nums[d[0]])
    
    return "\n".join(map(str, min_lst))


n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(slidingWindowMin(n, k, nums))


# print(n, k, nums)
# Входные данные
# 7 3
# 1 3 2 4 5 3 1
# Выходные данные
# 1
# 2
# 2
# 3
# 1