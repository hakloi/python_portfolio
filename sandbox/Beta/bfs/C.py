from collections import deque
n, m = map(int, input().split())

a = []
dist = []
D = deque()
for i in range(n):
    a.append(list(map(int, input().split())))
    dist.append([-1] * m)
    for j in range(m):
        if a[-1][j] == 1:
            dist[-1][j] = 0
            D.append((i, j))
            
while len(D) > 0:
    x, y = D.popleft()
    moves = [(-1, 0), (0,1), (1, 0), (0, -1)]
    for move in moves:
        x1, y1 = x + move[0], y + move[1]
        if 0 <= x1 <= n - 1 and 0 <= y1 <= m -1 and dist[x1][y1] == -1:
            dist[x1][y1] = dist[x][y] + 1 
            D.append((x1, y1))  

for row in dist:
    print(*row)  
