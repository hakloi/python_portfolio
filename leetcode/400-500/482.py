def licenseKeyFormatting(s, k):
    s = s.replace('-', '').upper()
    
    res = []
    for i in range(len(s)):
        if i % k == 0 and i != 0:
            res.append('-')
        res.append(s[-(i+1)])
        
    return ''.join(res[::-1])
    

print(licenseKeyFormatting("2-5g-3-J", 2))