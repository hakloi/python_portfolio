x = int(input())
n = int(input())
elements = []

for i in range(n):
    row = list(map(int, input().split()))
    elements.append(row)

m = len(elements[0]) #смотрим сколько было введено элементов,
                    # иначе если сделать m = n, то это будет ссылка на объект n 

for col in range(m):
    found = False
    for row in range(n):
        if elements[row][col] == x:
            found = True
            break
    if found:
        print("YES")
    else:
        print("NO")