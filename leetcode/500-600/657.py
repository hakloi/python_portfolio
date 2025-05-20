def judgeCircle(moves):
    x, y = 0, 0

    for s in moves:
        if s == "U":
            y += 1
        elif s == "D":
            y -= 1
        elif s == "L":
            x -= 1
        else:
            x += 1
    print(x, y)
    return (x == 0 and y == 0)
    
    
print(judgeCircle("DURDLDRRLL"))