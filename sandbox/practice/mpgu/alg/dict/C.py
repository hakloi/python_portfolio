n = int(input())
syns = {}

for i in range(n):
    phrase = input().split()
    syns[phrase[0]] = phrase[1]

syn = input()

for k, v in syns.items():
    if v == syn:
        print(k)
    elif k == syn:
        print(v)


# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# выходные данные
# Bye