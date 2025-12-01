def ideal_pair(cp, cp_cl, sh, sh_cl, tr, tr_cl, sho, sho_cl):
    i, j, k, m = 0, 0, 0, 0
    min_diff = float('inf')
    best_cp, best_sh, best_tr, best_sho = 0, 0, 0, 0
    
    while i < cp and j < sh and k < tr and m < sho:
        colors = [cp_cl[i], sh_cl[j], tr_cl[k], sho_cl[m]]
        min_cl = min(colors)
        max_cl = max(colors)
        diff = max_cl - min_cl
        
        if diff < min_diff:
            min_diff = diff
            best_cp, best_sh, best_tr, best_sho = cp_cl[i], sh_cl[j], tr_cl[k], sho_cl[m]
            
        if min_cl == cp_cl[i]:
            i += 1
        elif min_cl == sh_cl[j]:
            j += 1
        elif min_cl == tr_cl[k]:
            k += 1
        else:
            m += 1
    
    return best_cp, best_sh, best_tr, best_sho

caps = int(input())
cp_colors = list(map(int, input().split()))

shirts = int(input())
sh_colors = list(map(int, input().split()))

trousers = int(input())
tr_colors = list(map(int, input().split()))

shouse = int(input())
sho_colors = list(map(int, input().split()))

print(*ideal_pair(caps, cp_colors, shirts, sh_colors, trousers, tr_colors, shouse, sho_colors))