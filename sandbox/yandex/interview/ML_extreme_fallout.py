def dfs(matrix, x, y, N, visited):
    stack = [(x, y)]
    area = 0
    has_strong_precipitation = False
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        area += 1
        if matrix[cx][cy] >= T2:
            has_strong_precipitation = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and matrix[nx][ny] >= T1:
                stack.append((nx, ny))
    return area, has_strong_precipitation

def check_extreme_precipitation(N, T1, T2, K, matrix):
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= T1 and not visited[i][j]:
                area, has_strong_precipitation = dfs(matrix, i, j, N, visited)
                if area <= K and has_strong_precipitation:
                    continue
                else:
                    return False
    return True

N = int(input())
T1, T2, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

if check_extreme_precipitation(N, T1, T2, K, matrix):
    print("True")
else:
    print("False")
