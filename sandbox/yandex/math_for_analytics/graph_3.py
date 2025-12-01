import sys


def main():
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data.pop(0))
    
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        vertices = list(map(int, data[i].split()))
        for v in vertices:
            matrix[i][v] = 1
            
    for lst in matrix:
        print(" ".join(str(_) for _ in lst))
        
    


if __name__ == '__main__':
    main()
    
    
# 4

# 1 2
# 2
# 0