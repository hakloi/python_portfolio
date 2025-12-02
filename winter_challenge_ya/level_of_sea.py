import sys


def main():
    n = 10
    lst = [int(input()) for _ in range(n)]
    best_diff = float('inf')
    best_res = -1
    
    def dfs(i, curr_sum):
        nonlocal best_diff, best_res
        
        if i == 10:
            diff = abs(100 - curr_sum)
            if diff < best_diff or (diff == best_diff and curr_sum > best_res):
                best_diff = diff
                best_res = curr_sum
            return
        
        dfs(i + 1, curr_sum + lst[i])
        dfs(i + 1, curr_sum)
        
    dfs(0,0)
    return best_res



if __name__ == '__main__':
    main()
