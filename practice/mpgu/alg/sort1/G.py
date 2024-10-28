def insert_sort(lst, n):
    for i in range(1, n):
        insrt = False
        tmp = lst[i]
        j = i - 1
        while (j >= 0 and tmp < lst[j]):
            lst[j + 1] = lst[j]
            j = j - 1
            insrt = True
        lst[j + 1] = tmp
        if insrt:
            print(*lst)
        

n = int(input())
lst = list(map(int, input().split()))
insert_sort(lst, n)
