n = int(input())
mod_file = {}

for i in range(n):
    file = input().split()
    name = file.pop(0)
    mod_file[name] = file

m = int(input())

for j in range(m):
    operation, filename = input().split()
    if operation == 'write':
        if 'W' in mod_file.get(filename, []):
            print("OK")
        else:
            print("Access denied")
    elif operation == 'read':
        if 'R' in mod_file.get(filename, []):
            print("OK")
        else:
            print("Access denied")
    elif operation == 'execute':
        if 'X' in mod_file.get(filename, []):
            print("OK")
        else:
            print("Access denied")
        
