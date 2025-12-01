# Задана матрица K, содержащая n строк и m столбцов. 
# Седловой точкой этой матрицы назовем элемент, который 
# одновременно является минимумом в своей строке и максимумом в своем столбце.
n, m = map(int, input().split())
saddle_points = 0

matrix = [list(map(int, input().split())) for _ in range(n)]
        
row_min = [min(row) for row in matrix]
col_max = [max(matrix[i][j] for i in range(n)) for j in range(m)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
            saddle_points += 1

print(saddle_points)