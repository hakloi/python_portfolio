from collections import deque

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'S':
            start_x, start_y = i, j
        if maze[i][j] == 'F':
            end_x, end_y = i, j

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

queue = deque()
visited = set()

for direction in range(4):
    queue.append((start_x, start_y, direction, 0))
    visited.add((start_x, start_y, direction))

while queue:
    x, y, direction, steps = queue.popleft()

    if (x, y) == (end_x, end_y):
        print(steps)
        exit()

    dx, dy = moves[direction]
    nx, ny = x + dx, y + dy
    if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != 'X' and (nx, ny, direction) not in visited:
        visited.add((nx, ny, direction))
        queue.append((nx, ny, direction, steps + 1))

    new_direction = (direction + 1) % 4
    new_dx, new_dy = moves[new_direction]
    if 0 <= x + new_dx < r and 0 <= y + new_dy < c and maze[x + new_dx][y + new_dy] != 'X':
        if (x, y, new_direction) not in visited:
            visited.add((x, y, new_direction))
            queue.append((x, y, new_direction, steps + 1))

# 10 14
# XXXXXXXXXXXXXX
# X          XXX
# X XFXXXXX    X
# XXX   XX  XX X
# X S          X
# XX  XXXXXX X X
# X        X X X
# X X      X X X
# XXX XX       X
# XXXXXXXXXXXXXX
# Выходные данные
# 29