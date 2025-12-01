def archive(s, users):
    users.sort()
    
    summa = 0
    count = 0
    
    for mem in users:
        if summa + mem <= s:
            summa += mem
            count += 1
        else:
            break

    return count


s, n = map(int, input().split())
users = list(int(input()) for _ in range(n))
print(archive(s, users))