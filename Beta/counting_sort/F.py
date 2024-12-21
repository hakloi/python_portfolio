n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

presses = [0] * (n + 1)
for key in p:
    presses[key] += 1
    
print(presses)

for i in range(1, n + 1):
    if presses[i] > c[i - 1]:
        print("yes")
    else:
        print("no")