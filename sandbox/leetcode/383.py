from collections import Counter

def canConstruct(ransomNote, magazine):
    s1 = Counter(ransomNote)
    s2 = Counter(magazine)
    
    for k, v in s1.items():
        if s2[k] < v:
            return False
        
    return True

ransomNote = "aac"
magazine = "acccc"
print(canConstruct(ransomNote, magazine))