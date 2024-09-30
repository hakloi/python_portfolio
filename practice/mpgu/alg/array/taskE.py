n = int(input())
array = list(map(int, input().split()))
max_index = 0

for i in range(1, n):
    if array[i] > array[max_index]:
        max_index = i
print(max_index + 1)