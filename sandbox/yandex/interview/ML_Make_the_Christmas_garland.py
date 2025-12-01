# #  НЕВЕРНО

# from collections import deque
# from math import exp


# def find_farthest(n, graph, start):
#     q = deque([start])
#     dist = {start: 0}
#     farthest_node = start
    
#     while q:
#         node = q.popleft()
#         for neighbor, w in graph[node]:
#             if neighbor not in dist:
#                 dist[neighbor] = dist[node] + (1 / exp(w)) 
#                 q.append(neighbor)
#                 if dist[neighbor] > dist[farthest_node]:
#                     farthest_node = neighbor
                    
#     return farthest_node, dist


# def find_diameter(n, graph):
#     farthest_node, _ = find_farthest(n, graph, 1)
#     other_farthest, dist = find_farthest(n, graph, farthest_node)
#     path = []
#     node = other_farthest
#     while node != farthest_node:
#         path.append(node)
#         for neighbor, _ in graph[node]:
#             if neighbor in dist and dist[neighbor] < dist[node]:
#                 node = neighbor
#                 break
#     path.append(farthest_node)

#     path_length = len(path)
#     if path_length % 2 == 1:
#         return [path[path_length // 2]]
#     else:
#         return [path[path_length // 2 - 1], path[path_length // 2]]
 
    
# n = int(input())
# graph = {i: [] for i in range(1, n + 1)}

# for _ in range(n - 1):
#     a, b, t = map(int, input().split())
#     graph[a].append((b, t))
#     graph[b].append((a, t))
    

# centers = find_diameter(n, graph)
# print(min(centers))


# 10
# 2 7 2
# 2 8 7
# 8 6 4
# 8 5 8
# 7 4 6
# 2 3 2
# 6 1 6
# 8 10 7
# 2 9 2

# 8