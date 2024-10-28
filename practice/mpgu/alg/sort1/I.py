client_size = int(input())
shoe_sizes = sorted(map(int, input().split()))

count = 0 
last_size = client_size - 3 

for size in shoe_sizes:
    if size >= client_size and size >= last_size + 3:
        count += 1  
        last_size = size 

print(count)
