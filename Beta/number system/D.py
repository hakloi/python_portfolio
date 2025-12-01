def char_to_val(c):
    if c.isdigit():
        return int(c)
    return ord(c) - ord('A') + 10

def to_decimal(s, base):
    val = 0
    for ch in s:
        v = char_to_val(ch)
        if v >= base:
            return -1
        val = val * base + v
    return val

eq = input().strip()
A, rest = eq.split('+')
B, C = rest.split('=')

max_digit = max(max(A), max(B), max(C), key=lambda x: char_to_val(x))
min_base = char_to_val(max_digit) + 1
if min_base < 2:
    min_base = 2

answer = -1
for base in range(min_base, 37):
    a_dec = to_decimal(A, base)
    b_dec = to_decimal(B, base)
    c_dec = to_decimal(C, base)
    if a_dec == -1 or b_dec == -1 or c_dec == -1:
        continue
    if a_dec + b_dec == c_dec:
        answer = base
        break

print(answer)
