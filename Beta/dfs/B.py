n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = set()

def dfs(node, component):
    stack = [node]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            component.append(v)
            stack.extend(graph[v])

components = []

for v in range(1, n + 1):
    if v not in visited:
        component = []
        dfs(v, component)
        component.sort()  
        components.append(component)

print(len(components))
for component in components:
    print(len(component))
    print(*component)
