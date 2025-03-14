from collections import deque

def solve():
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    dist = [-1] * n
    parent = [-1] * n
    queue = deque([start])
    dist[start] = 0

    while queue:
        u = queue.popleft()
        for v in range(n):
            if adj_matrix[u][v] == 1 and dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    if dist[end] == -1:
        print(-1)
    elif dist[end] == 0:
        print(0)
    else:
        path = []
        current = end
        while current != -1:
            path.insert(0, current + 1)
            current = parent[current]

        print(dist[end])
        print(*path)


solve()