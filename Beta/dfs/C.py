def is_tree(matrix, n):
    edges = sum(sum(row) for row in matrix) // 2
    if edges != (n - 1):
        return "NO"
    
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbor in range(n):
            if matrix[node][neighbor] == 1:
                if neighbor not in visited:
                    if not dfs(neighbor, node):
                        return False
                elif neighbor != parent:
                    return False
        return True
    
    if not dfs(0, -1):
        return "NO"
    
    return "YES" if len(visited) == n else "NO"


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(is_tree(matrix, n))

# Входные данные
# 6
# 0 1 1 0 0 0
# 1 0 1 0 0 0
# 1 1 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# Выходные данные
# NO
# Входные данные
# 3
# 0 1 0
# 1 0 1
# 0 1 0
# Выходные данные
# YES