def firstUniqChar(s):

    dct = {}
    for char in s:
        dct[char] = dct.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if dct[char] == 1:
            return i
    
    return -1

    
print(firstUniqChar("leetcode"))