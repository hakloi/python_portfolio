def lengthAfterTransformations(s, t):
    
    while t != 0:
        new = ''
        for ch in s:
            if ch == 'z':
                new += 'ab'
            else:
                new += chr(ord(ch) + 1)
        s = new
        t -= 1
            
    
    return len(s)

s = "abcyy"
t = 2
print(lengthAfterTransformations(s, t))