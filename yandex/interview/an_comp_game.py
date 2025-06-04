from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

graph = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    indegree[v] += 1

dp = [0] * n
dp[0] = a[0]

queue = deque([i for i in range(n) if indegree[i] == 0])

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dp[v] < dp[u] + a[v]:
            dp[v] = dp[u] + a[v]
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)

print(max(dp))

