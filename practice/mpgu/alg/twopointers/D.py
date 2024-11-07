def ideal_pair(sh, sh_cl, tr, tr_cl):
    i, j = 0, 0
    min_diff = float('inf')
    best_sh, best_tr = 0, 0
    
    while i < sh and j < tr:
        diff = abs(sh_cl[i] - tr_cl[j])
        
        if diff < min_diff:
            min_diff = diff
            best_sh = sh_cl[i]
            best_tr = tr_cl[j]
            
        if sh_cl[i] > tr_cl[j]:
            j += 1
        elif sh_cl[i] < tr_cl[j]:
            i += 1
        else:
            return sh_cl[i], tr_cl[j]
    
    return best_sh, best_tr


shirts = int(input())
sh_colors = list(map(int, input().split()))

trousers = int(input())
tr_colors = list(map(int, input().split()))

print(*ideal_pair(shirts, sh_colors, trousers, tr_colors))
