def check_same_cards(arr):
    dct = {}
    min_diff = float('inf')
    for i, el in enumerate(arr):
        if el in dct:
            diff = i - dct[el] - 1
            min_diff = min(min_diff, diff)
        dct[el] = i
    
    if min_diff == float('inf'): return -1
    else: return min_diff

n = int(input())
arr = list(map(int, input().split()))
print(check_same_cards(arr))

# 5
# 1 3 2 1 4

# 2

# 6
# 1 7 2 9 11 15

# -1