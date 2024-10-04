# McCain 10
# McCain 5
# Obama 9
# Obama 8
# McCain 1

presidents = {}

with open('input.txt', 'r') as f:
    for line in f:
        name, votes = line.split() 
        if name in presidents:
            presidents[name] += int(votes)
        else:
            presidents[name] = int(votes)

for name in sorted(presidents):
    print(f"{name} {presidents[name]}")