def Euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def count_integer_points(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    return Euclid(dx, dy) + 1

x1, y1, x2, y2 = map(int, input().split())
print(count_integer_points(x1, y1, x2, y2))
