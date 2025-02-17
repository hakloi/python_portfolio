arr = [1, 2, 2, 3, 1, 2, 3, 4, 0, 10, 20]

start = 0
max_start = 0
max_end = 0
max_length = 1

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        if i - start > max_length:
            max_length = i - start
            max_start = start
            max_end = i - 1
        start = i

if len(arr) - start > max_length:
    max_length = len(arr) - start
    max_end = len(arr) - 1

print(arr[max_start:max_end + 1])
        