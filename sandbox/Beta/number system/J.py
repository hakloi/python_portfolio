def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def sum(a, b, c, d):
    num = a * b + c * b
    denum = b * d

s = input()
if '.' not in s:
    print(int(s, 2), 1)
elif '(' not in s:
    x = int(s[:s.find('.')], 2)
    s = s[s.find('.') + 1:]
    res = (0, 0)
    for i in range(len(s)):
        if s[i] == '1':
            res = sum(res[0], res[1], 1, 2 ** (i + 1))
    res = sum(res[0], res[1], x, 1)
    print(res)
            