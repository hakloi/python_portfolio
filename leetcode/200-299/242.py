def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    s_lst = sorted(list([el for el in s]))
    t_lst = sorted(list([el for el in t]))
    
    for i in range(len(s_lst)):
        if s_lst[i] != t_lst[i]:
            return False
        
    return True
    # print(s_lst, t_lst)
    
    
    
    # for char in s:
    #     if t.find(char) == -1:
    #         return False

    # return True
    

s = "anagramk"
t = "nagarame"
print(isAnagram(s, t))
print(isAnagram("aacc", "ccac"))