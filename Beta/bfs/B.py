from collections import deque

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

def bfs(N, start, end):
    queue = deque([(start[0], start[1], 0)]) 
    visited = set()
    visited.add(start)
    parent = {}  

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            path = []
            while (x, y) in parent:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return steps, path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= N and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)  

    return -1, [] 

N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

steps, path = bfs(N, (x1, y1), (x2, y2))

print(steps)
for x, y in path:
    print(x, y)
