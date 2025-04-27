from collections import defaultdict

def countLargestGroup(n):
    groups = defaultdict(list)
    
    for i in range(1, n + 1):
        s = sum(int(el) for el in str(i))
        groups[s].append(i)
        
    max_size = max(len(v) for k, v in groups.items())
    
    return  sum(1 for v in groups.values() if len(v) == max_size)
    
    
    
print(countLargestGroup(13))