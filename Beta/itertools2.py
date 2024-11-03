# not a or b and c
import itertools

exp = input()

print("a b c f")

for a, b, c in itertools.product([0, 1], repeat = 3):
    res = eval(exp)
    print(f"{a} {b} {c} {int(res)}")