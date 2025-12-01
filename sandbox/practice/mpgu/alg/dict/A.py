n = int(input())
clients = {}

for i in range(n):
    request = input().split()
    op = request[0]
    if op == '1':
        name = request[1] 
        amount = int(request[2])
        if name in clients:
            clients[name] += amount
        else:
            clients[name] = amount
            
    elif op == '2':
        name = request[1] 
        if name in clients:
            print(clients[name])
        else:
            print("ERROR")