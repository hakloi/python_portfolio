def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a   

n1, n2 = map(int, input().split())
print(nod(n1, n2))