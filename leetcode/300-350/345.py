def reverseVowels(s):
    word = list(s)
    vowels = "aeiouAEIOU"
    l, r = 0, len(s) - 1
    
    while l < r:
        if word[l] not in vowels:
            l += 1
        elif word[r] not in vowels:
            r -= 1
        else:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
            
    return "".join(_ for _ in word)
                
    

print(reverseVowels("IceCreAm"))
# print(ord('A'), ord('Z'), ord('a'), ord('z'))