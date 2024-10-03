word = input()
n = len(word)

first = word[:(n + 1) // 2] # hello -> 5 -> (5 + 1) // 2 = 3 -> до :3
second = word[(n + 1) // 2:] # (5 + 1) // 2 -> 3 -> с позиции 3 до конца

print(second + first)


# lj = [1, 20, 3, 7, 5]

# print(sorted(lj))
# print(lj)

# res = lj.sort()
# print(lj)