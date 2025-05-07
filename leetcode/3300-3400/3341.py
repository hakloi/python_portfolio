import heapq


def minTimeToReach(mT):
    m = len(mT)
    n = len(mT[0])
    
    dp = [[float('inf')] * m for _ in range(n)]
    
    heap = []
    # row, col, time = 0, 0, 0
    heapq.heappush(heap, (0, 0, 0))
    
    # (1, 0) - next row 
    # (0, 1) - next col 
    # (-1, 0) - prev row 
    # (0, -1) - prev col
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    print(m, n)
    print(dp)
    
    while heap:
        curr_time, row, col = heapq.heappop(heap)
        
        if curr_time >= dp[row][col]:
            continue
        
        dp[row][col] = curr_time
        
        if row == (n - 1) and col == (m - 1):
            return curr_time
        
        for dr, dc in dirs:
            new_row = row + dr
            new_col = col + dc
            
            if 0 <= new_row < n and 0 <= new_col < m:
                if dp[new_row][new_col] == float('inf'):
                    wait_time = max(mT[new_row][new_col], curr_time)
                    time = wait_time + 1
                    heapq.heappush(heap, (time, new_row, new_col))
                    
    return -1 
    
    
    
    
    
moveTime = [[0,1],[1,2]]
print(minTimeToReach(moveTime))