def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
x = a // b
a = a % b
first = bin(x)[2:]

if a == 0:
    print(first)
else:
    d = dict()
    second = ''
    while a != 0:
        g = gcd(a, b)
        a, b = a // g, b // g
        if (a, b) not in d:
            d[(a, b)] = len(second)
            a *= 2
            second += str(a//b)
            a = a % b
        else:
            print(first + '.' + second[:d[(a, b)]] + '(' + second[d[(a, b)]:] + ')')
            exit(0)
    print(first + '.' + second)