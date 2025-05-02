def pushDominoes(s):
    s = 'L' + s + 'R'
    res = ''
    prev = 0
    for curr in range(1, len(s)):
        if s[curr] == '.':
            continue
        span = curr - prev - 1
        if prev > 0:
            res += s[prev]
        if s[curr] == s[prev]:
            res += s[prev] * span
        elif s[prev] == 'L' and s[curr] == 'R':
            res += '.' * span
        else:
            res += 'R' * (span // 2) + '.' * (span % 2) + 'L' * (span // 2)
        prev = curr

    return res
        

print(pushDominoes("RR.L"))
# Output: "RR.L"

print(pushDominoes(".L.R...LR..L.."))
# Output: "LL.RR.LLRRLL.."

 