from collections import Counter

def longestPalindrome(words):
    cnt = Counter(words)
    ln = 0
    used_center = False
    
    for word in cnt:
        rev = word[::-1]
        if word == rev:
            pairs = cnt[word] // 2
            ln += pairs * 4
            if cnt[word] % 2 == 1:
                used_center = True
        elif rev in cnt:
            pairs = min(cnt[word], cnt[rev])
            ln += pairs * 4
            cnt[rev] = 0
    
    if used_center:
        ln += 2
    
    return ln
        
    
words = ["lc","cl","gg"]
print(longestPalindrome(words))