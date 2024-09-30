n = int(input())
list_id = list(map(int, input().split()))

new_list_id = sorted(list_id)
print(new_list_id[0], new_list_id[1])