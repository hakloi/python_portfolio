strs = ["dog","racecar","car"]

common = strs[0]

for word in strs[1:]:
    prefix = ""
    for i in range(min(len(common), len(word))):
        if common[i] == word[i]:
            prefix += common[i]
        else:
            break
        
    common = prefix

    if common == "":
        break
    
print(common) 
            