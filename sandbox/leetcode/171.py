def titleToNumber(columnTitle):
    letters = list(columnTitle)
    
    res = 0
    for letter in letters:
        res = res * 26 + (ord(letter) - ord('A') + 1)
        
    return res

print(titleToNumber("FXSHRXW"))
# 2147483647
print(titleToNumber("ZY"))

# print(ord("A") % 64)
