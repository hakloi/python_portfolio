# with open("input.txt", "r", encoding="utf-8") as file, \
#     open("output.txt", "w", encoding="utf-8") as fileout:
#     line = file.read().strip().split()
#     res = int(line[0]) + int(line[1])
    
#     fileout.write(str(res))

# from sys import stdin

# a, b = map(int, stdin.read().strip().split())

# print(a + b)

j = input()
s = input()

j_set = set(j)
cnt = 0

for char in s:
    if char in j_set:
        cnt += 1
        
print(cnt)
# ab
# aabbccd