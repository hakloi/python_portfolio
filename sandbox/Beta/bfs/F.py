from collections import deque

a = int(input())
b = int(input())
dist = [-1] * 10000
dist[a] = 0
prev = [-1] * 10000

D = deque()
D.append(a)
while len(D) > 0:
    x = D.popleft()
    if (x // 1000 < 9):
        if dist[x + 1000] == -1:
            dist[x + 1000] = dist[x] + 1
            prev[x + 1000] = x
            D.append(x + 1000)
    if (x % 10 > 1):
        if dist[x - 1] == -1:
            dist[x - 1] = dist[x] + 1
            prev[x - 1] = x
            D.append(x - 1)
    if dist[x % 10 * 1000 + x // 10] == -1:
            dist[x % 10 * 1000 + x // 10] = dist[x] + 1
            prev[x % 10 * 1000 + x // 10] = x
            D.append(x % 10 * 1000 + x // 10)
    if dist[x % 1000 * 10 + x // 1000] == -1:
            dist[x % 1000 * 10 + x // 1000] = dist[x] + 1
            prev[x % 1000 * 10 + x // 1000] = x
            D.append(x % 1000 * 10 + x // 1000)


ans = []
while b != -1:
    ans.append(b)
    b = prev[b]
ans = ans[::-1]

for x in ans:
    print(x)