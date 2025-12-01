def Evaluate(s):
    res = int(s[0])
    for i in range(1, len(s), 2):
        if s[i] == '+':
            res += int(s[i + 1])
        elif s[i] == '-':
            res -= int(s[i + 1])
    return res

s = input()
print(Evaluate(s))