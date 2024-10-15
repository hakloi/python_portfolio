vaults = {}

def deposit(name, sum):
    if name not in vaults:
        vaults[name] = 0
    vaults[name] += sum

def withdraw(name, sum):
    if name not in vaults:
        vaults[name] = 0
    vaults[name] -= sum

def balance(name):
    if name in vaults:
        print(vaults[name])
    else:
        print("ERROR")

def transfer(name1, name2, sum):
    if name1 not in vaults:
        vaults[name1] = 0
    if name2 not in vaults:
        vaults[name2] = 0
    vaults[name1] -= sum
    vaults[name2] += sum

def income(p):
    for name in vaults:
        if vaults[name] > 0:
            vaults[name] += vaults[name] * p // 100

with open("input.txt", "r") as f:
    for line in f:
        request = line.split()
        if request[0] == 'DEPOSIT':
            name, sum = request[1], int(request[2])
            deposit(name, sum)
        elif request[0] == 'WITHDRAW':
            name, sum = request[1], int(request[2])
            withdraw(name, sum)
        elif request[0] == 'BALANCE':
            name = request[1]
            balance(name)
        elif request[0] == 'TRANSFER':
            name1, name2, sum = request[1], request[2], int(request[3])
            transfer(name1, name2, sum)
        elif request[0] == 'INCOME':
            p = int(request[1])
            income(p)