def bubble_sort(lst, n):
    cnt = 0
    for i in range(n):
        for j in range(1, n - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                cnt += 1
    return cnt


n = int(input())
lst = list(map(int, input().split()))
print(bubble_sort(lst, n))