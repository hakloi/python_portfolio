def f2(a, n, x):
    if (n == 0):
        return 0
    elif (a[n-1] == x):
        return 1 + f2(a, n - 1, x)
    return f2(a, n - 1, x)


a = [5, 4, 3, 2, 1, 2, 3, 4, 5]
n = len(a)
print(f2(a, 9, 3))