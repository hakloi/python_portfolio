n = int(input())
array = list(map(int, input().split()))
target = int(input())
count_list = []

for i in range(len(array)):
    if array[i] == target:
        count_list.append(i + 1)
print(*count_list)