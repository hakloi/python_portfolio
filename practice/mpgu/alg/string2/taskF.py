def CountWords(s):
    count = 0
    inword = False
    
    for el in s:
        if el.isalpha():
            if not inword:
                count += 1
                inword = True
        else:
            inword = False
    return count

s = input()
print(CountWords(s))