def LongestWord (s):
    longestword = ''
    currentword = ''
    for el in s:
        if el.isalpha():
            currentword += el
        else: 
            if len(currentword) > len(longestword):
                longestword = currentword
            currentword = ''
    if len(currentword) > len(longestword):
        longestword = currentword
    return longestword
    


s = input()
print(LongestWord(s))
