j = input().strip()
s = input().strip()
cnt = 0

for i in s:
    if i in j:
        cnt += 1
            
print(cnt) 