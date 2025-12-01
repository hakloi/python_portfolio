from collections import deque

def chess_to_index(chess_pos):
    col, row = chess_pos
    return ord(col) - ord('a'), int(row) - 1

s1, s2 = input().split()
x1, y1 = chess_to_index(s1)
x2, y2 = chess_to_index(s2)

dist = {}
dist[(x1, y1, x2, y2)] = 0
D = deque()
D.append([x1, y1, x2, y2])

moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

while D:
    x1, y1, x2, y2 = D.popleft()

    if x1 == x2 and y1 == y2:
        print(dist[(x1, y1, x2, y2)])
        break

    for dx1, dy1 in moves:
        for dx2, dy2 in moves:
            nx1, ny1 = x1 + dx1, y1 + dy1
            nx2, ny2 = x2 + dx2, y2 + dy2

            if 0 <= nx1 < 8 and 0 <= ny1 < 8 and 0 <= nx2 < 8 and 0 <= ny2 < 8:
                if (nx1, ny1, nx2, ny2) not in dist:
                    dist[(nx1, ny1, nx2, ny2)] = dist[(x1, y1, x2, y2)] + 1
                    D.append([nx1, ny1, nx2, ny2])
else:
    print(-1)
