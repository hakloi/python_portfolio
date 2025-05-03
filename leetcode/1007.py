def func(tops, bottoms):
    def check(x):
        rot_t, rot_b = 0, 0
        
        for i in range(len(tops)):
            if tops[i] != x and bottoms[i] != x:
                return float('inf')
            elif tops[i] != x:
                rot_t += 1
            elif bottoms[i] != x:
                rot_b += 1
        return min(rot_b, rot_t)
    
    res = min(check(tops[0]), check(bottoms[0]))
    return res if res != float('inf') else -1

tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(func(tops, bottoms))