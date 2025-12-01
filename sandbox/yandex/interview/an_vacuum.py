def main():
    N, M, x, y = map(int, input().split())
    grid = [input().strip() for _ in range(M)]

    free_cells = sum(row.count('0') for row in grid)

    # if free_cells == 0:
    #     print(0)
    #     return

    # if x >= 2 * y:
    #     time = free_cells * y
    # else:
    #     time = free_cells * y + (free_cells - 1) * x
    if free_cells <= 1:
        print(free_cells * y)
        return
    else:
        result = (free_cells - 1) * x + free_cells * y
        print(result)
        return

if __name__ == "__main__":
    main()
