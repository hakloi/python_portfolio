from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

queue = deque()
queue.append((0, 0, 0))

visited  = set()
visited.add((0,0))

moves = [(-1, 0), (0, 1), (0, -1), (1, 0)]

while queue:
    x, y, steps = queue.popleft()
    
    for dx, dy in moves:
        nx, ny = x, y

        while (0 <= nx + dx < n) and (0 <= ny + dy < m) and arr[nx + dx][ny + dy] != 1: 
            nx += dx 
            ny += dy
            if arr[nx][ny] == 2:
                print(steps + 1)
                exit()
                
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            queue.append((nx, ny, steps + 1))
# Входные данные
# 4 5
# 0 0 0 0 1
# 0 1 1 0 2
# 0 2 1 0 0
# 0 0 1 0 0

# Выходные данные
# 3
