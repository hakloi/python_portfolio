def setZeroes(matrix):
    rows = set()
    cols = set()
    
    for i in range(matrix):
        for j in range(matrix[0]):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
                
            
    
    
    # return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]