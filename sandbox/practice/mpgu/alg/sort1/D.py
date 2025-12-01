def insertion_sort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i - 1
        while (j >= 0 and tmp < lst[j]):
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = tmp
        
    return lst


n = int(input())
lst = list(map(int, input().split()))
res = insertion_sort(lst)

print(*res)