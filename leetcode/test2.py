n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input().strip()))

max_len = 0
current_len = 0
for num in nums:
    if num == 1:
        current_len += 1
        max_len = max(current_len, max_len)
    else:
        current_len = 0
        
print(max_len)

# 5
# 1
# 0
# 1
# 0
# 1
