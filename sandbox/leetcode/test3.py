n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input().strip()))
    
upt_nums = sorted(list(set(nums)))

# print(upt_nums)
print(*upt_nums, sep="\n")

