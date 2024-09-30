res = list(map(int, input().split()))
seen = set()

for i in range(len(res)):
    if res[i] in seen:
        print('YES')
    else: 
        seen.add(res[i])
        print('NO')