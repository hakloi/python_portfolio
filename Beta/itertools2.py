# not a or b and c
# import itertools

# exp = input()

# print("a b c f")

# for a, b, c in itertools.product([0, 1], repeat = 3):
#     res = eval(exp)
#     print(f"{a} {b} {c} {int(res)}")


# not A or B and C
import itertools
exp = input()

vars = sorted(set(filter(str.isupper, exp)))

print(" ".join(vars) + " F")

for values in itertools.product([0, 1], repeat=len(vars)):
    local = dict(zip(vars, values))
    res = eval(exp, {}, local)
    print(" ".join(map(str, values)), int(res))
    
    
# A B C F
# 0 0 0 1
# 0 0 1 1
# 0 1 0 1
# 0 1 1 1
# 1 0 0 0
# 1 0 1 0
# 1 1 0 0
# 1 1 1 1