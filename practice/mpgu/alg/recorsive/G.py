def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    else:
        return a * power(a, n - 1)

a = float(input())
n = int(input())
res = power(a, n)

if a.is_integer() and n >= 0:
    res = int(res)
    print(res)
else:
    print(f'{res:.5f}')


# Примеры
# входные данные
# 2
# 7
# выходные данные
# 128
# входные данные
# 1.00001
# 100000
# выходные данные
# 2.71827