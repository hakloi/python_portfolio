def findWordsContaining(words, x):
    if not words:
        return []

    return [i for i, word in enumerate(words) if x in word]
    
print(findWordsContaining(["abc","bcd","aaaa","cbc"], 'a'))