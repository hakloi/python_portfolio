def numEquivDominoPairs(dominoes):
    dct = {}
    for pair in dominoes:
        pair.sort()
        # print(pair)
        s = f"{pair[0]}-{pair[1]}"
        if s not in dct:
            dct[s] = 1
        else:
            dct[s] += 1
    
    res = max(v for v in dct.values())   
    # for k, v in dct.items():
    #     print(k, v) 
    return res
    
    
dominoes = [[1,2],[2,1],[3,4],[5,6]]
dominoes2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# print(numEquivDominoPairs(dominoes))
print(numEquivDominoPairs(dominoes2))