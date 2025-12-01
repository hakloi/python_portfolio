import sys


def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = len(data)
    matrix = []
    
    for line in data:
        matrix.append(list(map(int, line.split())))
        
    mtx_list = []
    
    for i in range(n): 
        s = ""
        for j in range(n):
            if matrix[i][j] == 1:
                s += f"{j} "  
        mtx_list.append(s)
    
    print(*mtx_list, sep="\n")

    


if __name__ == '__main__':
    main()