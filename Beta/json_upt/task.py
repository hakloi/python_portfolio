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
