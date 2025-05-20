def findRestaurant(lst1, lst2):
    ind_map = {name: i for i, name in enumerate(lst1)}
    res_sum = float('inf')
    res = []
    
    for j, name in enumerate(lst2):
        if name in ind_map:
            i = ind_map[name]
            diff = abs(i - j)
            if diff < res_sum:
                res = [name]
            elif diff == res_sum:
                res.append(name)
            
    return res
                
    