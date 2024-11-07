def substr_count(w, n, k):
    i, j = 0, 0
    dct = {}
    max_len = 0
    start_ind = 0
    
    for j in range(n):
        dct[w[j]] = dct.get(w[j], 0) + 1
        
        while any(count > k for count in dct.values()):
            dct[w[i]] -= 1
            if dct[w[i]] == 0:
                del dct[w[i]]
            i += 1
        
        if j - i + 1 > max_len:
            max_len = j - i + 1
            start_ind = i + 1
    
    return max_len, start_ind
    

n, k = map(int, input().split())
w = input()
print(*substr_count(w, n, k))

# 3 1
# abb
# Выходные данные
# 2 1