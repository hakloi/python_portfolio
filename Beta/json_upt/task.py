# import json
# from sys import stdin

# f1 = input()

# with open(f1, "r", encoding="utf-8") as filein:
#     records = json.load(filein)

# for line in stdin:
#     a, b = line.replace(" ", "").split('==')
#     records[a] = b.strip("\n")


# with open(f1, "w", encoding="utf-8") as fileout:
#     json.dump(records, fileout, ensure_ascii=False, indent=4)

# data.json
# one == один
# two == два
# three == три

# def print_hello(name):
#     return "Hello, " + name + "!"

# name = "Yandex"
# print(print_hello(name))

    # dct = {k: v for k, v in items}
    # res = []
    
    # for j in queries:
    #     max_v = None
    #     for k, v in dct.items():
    #         if j >= k:
    #             if max_v is None or v > max_v:
    #                 max_v = v
    #     res.append(max_v)
    


# queries = [1,2,3,4,5,6]
# items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
# print(func(items, queries))


# def majorityElement(nums):
#         dct = {}

#         for el in nums:
#             dct[el] = dct.get(el, 0) + 1

#         max_k = max(dct, key=dct.get)
        
#         return max_k
        
# nums = [2,2,1,1,1,2,2]
# print(majorityElement(nums))

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)


# result = gcd(12, 45)
# print(result)


# print(45 % 12, 12 * 9)

# import itertools

# def implication(a, b):
#     return not a or b

# def disjunction(a, b):
#     return a != b

# def equation(a, b):
#     return a == b
    

# exp = input()
# vars = sorted(set(filter(str.isupper, exp)))

# print(" ".join(vars) + " F")

# exp = exp.replace("->", "implication").replace("^", "disjunction").replace("~", "equation")

# for values in itertools.product([0, 1], repeat=len(vars)):
#     local_vars = dict(zip(vars, values))
    
#     eval_exp = exp
#     for var, val in local_vars.items():
#         eval_exp = eval_exp.replace(var, str(val))
        
#     F = eval(eval_exp, {"implication": implication, "disjunction": disjunction, "equation": equation})
    
#     print(" ".join(map(str, values)) + " " + str(int(F)))

