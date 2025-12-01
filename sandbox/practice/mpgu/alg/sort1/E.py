# 5
# 5 4 3 2 1

def bubble_sort(lst, n):
    for i in range(n):
        for j in range(1, n - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
        
    
    return lst

n = int(input())
lst = list(map(int, input().split()))

res = bubble_sort(lst, n)
print(*res)