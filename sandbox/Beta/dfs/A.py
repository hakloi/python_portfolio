def dfs(node, graph, visited):
    visited[node] = True
    count = 1  
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            count += dfs(neighbor, graph, visited)  # Рекурсивно проходим дальше
    return count

N, S = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]  

visited = [False] * N

result = dfs(S - 1, graph, visited)

print(result) 


# Входные данные
# 3 1
# 0 1 1
# 1 0 0
# 1 0 0
# Выходные данные
# 3