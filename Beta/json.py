# from sys import stdin

# lines = stdin.read().strip().splitlines()
# lst = sum([sum(map(int, line.split())) for line in lines])

# print(lst)


# 1 2
# 3 4 5
# 6
# 7 8 9 10

# from sys import stdin

# lines = stdin.read().strip().splitlines()
# lst = [line.split()[1:] for line in lines]

# res = []
# for v in lst:
#     diff = abs(int(v[0]) - int(v[1]))
#     res.append(diff)
    
# result = round(sum(res) / len(res))
# print(result)
    
    
# from sys import stdin

# lines = stdin.read().strip().splitlines()

# res = []

# for line in lines:
#     line.split()
#     if "#" in line:
#         ind = line.index("#")
#         if ind != 0:
#             res.append(line[:ind].rstrip())
#     else:
#         res.append(line)
        
# print(*res, sep="\n")
        
        
# from sys import stdin

# lines = stdin.read().strip().splitlines()
# target = lines[-1]

# for line in lines:
#     if target.lower() in line.lower():
#         print(line)


# from sys import stdin

# lines = stdin.read().strip().splitlines()

# res = [line.split() for line in lines]

# result = []

# for v in res:
#     for i in v:
#         if i.lower() == i.lower()[::-1]:
#             result.append(i)

# result = sorted(list(set(result)))

# print(*result, sep="\n")